"""Tests for the versioned-docs assembler in ``tools/build_docs.py``.

``tools/`` is a scripts directory, not part of the installed package, so the
module is loaded from its path rather than imported by name.

The one behaviour worth pinning here is the failure mode that silently destroys
published documentation: the release deploy cleans ``gh-pages`` of everything the
assembled site omits, so a version dropped because ``git archive`` errored is a
version deleted.
"""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

_BUILD_DOCS = Path(__file__).parents[1] / "tools" / "build_docs.py"


def _load() -> ModuleType:
    """Load ``tools/build_docs.py`` as a module.

    Returns:
        The loaded module.
    """
    spec = importlib.util.spec_from_file_location("build_docs", _BUILD_DOCS)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fail(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
    """Stand in for a ``git archive`` invocation that errors.

    Returns:
        A completed process carrying a non-zero return code.
    """
    return subprocess.CompletedProcess(args=[], returncode=128, stdout=b"", stderr=b"boom")


def test_published_version_failure_aborts(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """A published version that cannot be archived fails instead of vanishing."""
    module = _load()
    monkeypatch.setattr(module.subprocess, "run", _fail)

    with pytest.raises(RuntimeError, match="0.1"):
        module.preserve_from_gh_pages("0.1", tmp_path, "origin/gh-pages", required=True)


def test_optional_alias_failure_is_tolerated(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """The optional ``latest`` alias may be absent without failing the build."""
    module = _load()
    monkeypatch.setattr(module.subprocess, "run", _fail)

    module.preserve_from_gh_pages("latest", tmp_path, "origin/gh-pages", required=False)
