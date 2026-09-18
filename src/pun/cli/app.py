"""CLI application for the project.

The ``pun`` command is the single Typer root. Every enabled
component other than the primary (CLI > GUI > TUI > web > MCP > worker) is hung
off it as a lazily-imported subcommand — ``pun interactive``
(TUI), ``pun web``, ``pun mcp``, ... — rather
than a separate ``pun-<name>`` console script (see ADR-019).
"""
# mypy: disable-error-code="misc"

from __future__ import annotations

import platform
from importlib.metadata import Distribution, PackageNotFoundError

import typer

from pun.__metadata__ import PROJECT_NAME
from pun.core.logging_setup import get_logger

__all__ = ["app", "info", "interactive", "show_version"]

logger = get_logger()

app = typer.Typer(name="pun", no_args_is_help=True)


@app.command(name="version")
def show_version() -> None:
    """Show the current version number of pun.

    Show the version number:
        pun version

    Example output:
        0.1.0

    Raises:
        typer.Exit: If the package metadata cannot be found.
    """
    try:
        distribution = Distribution.from_name(PROJECT_NAME)
    except PackageNotFoundError:
        # An uninstalled or partial package is an expected, user-facing error, so
        # log without the traceback that logging.exception would add.
        logger.error("Package metadata not found for %s", PROJECT_NAME)  # noqa: TRY400
        typer.echo(
            f"Error: Package '{PROJECT_NAME}' metadata not found. Is the package installed correctly?",  # noqa: E501
            err=True,
        )
        raise typer.Exit(code=1) from None
    logger.info("Command `version` called.")
    typer.echo(distribution.version)
    logger.info("Version displayed successfully.")


@app.command()
def info() -> None:
    """Display information about the pun application.

    Show application information:
        pun info

    Example output:
        Application Version: 0.1.0
        Python Version: 3.12.0 (CPython)
        Platform: Darwin

    Raises:
        typer.Exit: If the package metadata cannot be found.
    """
    try:
        distribution = Distribution.from_name(PROJECT_NAME)
    except PackageNotFoundError:
        # An uninstalled or partial package is an expected, user-facing error, so
        # log without the traceback that logging.exception would add.
        logger.error("Package metadata not found for %s", PROJECT_NAME)  # noqa: TRY400
        typer.echo(
            f"Error: Package '{PROJECT_NAME}' metadata not found. Is the package installed correctly?",  # noqa: E501
            err=True,
        )
        raise typer.Exit(code=1) from None
    logger.info("Command `info` called.")
    python_version = platform.python_version()
    python_implementation = platform.python_implementation()
    typer.echo(f"Application Version: {distribution.version}")
    typer.echo(f"Python Version: {python_version} ({python_implementation})")
    typer.echo(f"Platform: {platform.system()}")
    logger.info("Application information displayed successfully.")


@app.command()
def interactive() -> None:  # pragma: no cover
    """Start interactive mode (TUI) for pun.

    Launch the terminal user interface:
        pun interactive

    Raises:
        typer.Exit: Propagating the TUI's exit code.
    """
    from pun.tui.app import main  # noqa: PLC0415

    raise typer.Exit(code=main())
