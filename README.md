# pun

<!-- TODO @hasansezertasan: Make it work, make it right, make it fast. -->
[![CI](https://github.com/hasansezertasan/pun/actions/workflows/ci.yml/badge.svg)](https://github.com/hasansezertasan/pun/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/hasansezertasan/pun)](https://codecov.io/gh/hasansezertasan/pun)
[![Documentation Status](https://img.shields.io/github/deployments/hasansezertasan/pun/github-pages?label=docs)](https://hasansezertasan.github.io/pun)
[![PyPI - Version](https://img.shields.io/pypi/v/pun.svg)](https://pypi.org/project/pun)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pun.svg)](https://pypi.org/project/pun)
[![License - MIT](https://img.shields.io/github/license/hasansezertasan/pun.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/hasansezertasan/pun?style=social)](https://github.com/hasansezertasan/pun/stargazers)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/pun)](https://github.com/hasansezertasan/pun)

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/hasansezertasan/pun/badge)](https://scorecard.dev/viewer/?uri=github.com/hasansezertasan/pun)
[![GitHub Tag](https://img.shields.io/github/tag/hasansezertasan/pun?include_prereleases=&sort=semver&color=black)](https://github.com/hasansezertasan/pun/releases/)

[![Downloads](https://pepy.tech/badge/pun)](https://pepy.tech/project/pun)
[![Downloads/Month](https://pepy.tech/badge/pun/month)](https://pepy.tech/project/pun)
[![Downloads/Week](https://pepy.tech/badge/pun/week)](https://pepy.tech/project/pun)

> This is a pun.

-----

## Table of Contents

- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support-heart)
- [Motivation](#motivation)
- [Features](#features)
- [About](#about)
- [Author](#author-person_with_crown)
- [Analysis](#analysis)
- [Contributing](#contributing-heart)
- [Development](#development-toolbox)
- [Releasing](#releasing)
- [Credits](#credits)
- [License](#license-scroll)
- [Changelog](#changelog-memo)

## Screenshots

<!-- TODO @hasansezertasan: Add screenshots or a demo GIF, or remove this section. -->

## Installation

`pun` is a standalone end-user tool whose primary command is `pun`. Install it into an isolated environment:

```console
uv tool install pun
```

Or run it without installing with `uvx pun`. See the [installation docs](https://hasansezertasan.github.io/pun/installation.html) for pipx and from-source options.

### Verify the installation

The package root is importable after installation:

```pycon
>>> from pun import __doc__
>>> isinstance(__doc__, str)
True

```

<!--
TODO @hasansezertasan: Add project-specific, runnable examples here.

pytest runs the pycon examples in this file (--doctest-glob=README.md).
doctest cannot see Markdown and ends an example's expected output at the first
blank line, so leave a blank line before every closing fence -- as the example
above does. Without it the closing delimiter is read as part of the expected
output and the example fails ("Expected: 2 / Got: 2"). Examples with no output
line at all need the blank line too.
-->
## Usage

### CLI

```bash
pun version
pun info
```

### TUI

```bash
pun interactive
```

An interactive terminal user interface displays project information. Press 'q' to exit.

## Support :heart:

If you have any questions or need help, feel free to open an issue on the [GitHub repository][pun].

## Motivation

<!-- TODO @hasansezertasan: Explain why this project exists and what problem it solves, or remove this section. -->

## Features

- **CLI Application**: Command-line interface built with Typer
- **TUI Application**: Terminal user interface built with Textual
- **Configuration Management**: Type-safe settings using Pydantic

## About

<!-- TODO @hasansezertasan: Add background/context about the project, or remove this section. -->

## Author :person_with_crown:

This project is maintained by [Hasan Sezer Taşan][author], It's me :wave:

## Analysis

- [Snyk Python Package Health Analysis](https://snyk.io/advisor/python/pun)
- [Libraries.io - PyPI](https://libraries.io/pypi/pun)
- [Safety DB](https://data.safetycli.com/packages/pypi/pun)
- [PePy Download Stats](https://www.pepy.tech/projects/pun)
- [PyPI Download Stats](https://pypistats.org/packages/pun)
- [Pip Trends Download Stats](https://piptrends.com/package/pun)
- [PyPI Map Dependency Graph](https://pypimap.com/package/pun)

## Contributing :heart:

Any contributions are welcome! Please follow the [Contributing Guidelines](./.github/CONTRIBUTING.md) to contribute to this project.

## Development :toolbox:

See the [Contributing Guidelines](./.github/CONTRIBUTING.md#your-first-code-contribution)
for local setup, the common development tasks (exposed via [mise](https://mise.jdx.dev)),
building and previewing the documentation, and the VS Code debugging configurations.

## Releasing

Versioning and releases are automated with [release-please](https://github.com/googleapis/release-please), driven by [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) PR titles squash-merged into `main`. release-please maintains a release PR that bumps the version and `CHANGELOG.md`; merging it tags the release and publishes to PyPI. See the [Contributing Guidelines](./.github/CONTRIBUTING.md#releasing) for the commit conventions, and the [Repository setup](./docs/maintaining/setup.rst) guide for one-time configuration and optional post-launch integrations such as a social preview, downstream packaging, and Repology.

Pause merges that change `.github/workflows/`, including Renovate action-pin updates, from merging a release PR until the entire Release run finishes. Workflow differences between the release commit and current `main` can block tag or release creation with a 403 when using `GITHUB_TOKEN`. See [Release recovery](./docs/maintaining/setup.rst#keep-workflow-changes-out-of-an-active-release) for prevention and recovery steps.

For adoption or template-update reconciliation, ask your agent to "audit this
template adoption/update against our existing project behavior".
The shipped [template-adoption skill](./.claude/skills/template-adoption/SKILL.md)
also supports audits after an update was applied. It compares workflow behavior,
required checks, custom tooling, and documentation, and asks before consequential
cleanup. Its prek-workflow example shows why duplicate commands alone do not
justify removing a workflow. Use the sibling `repo-setup` skill for repository
settings and release setup.

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [hasansezertasan/copier-pyproject](https://github.com/hasansezertasan/copier-pyproject) project template.

## License :scroll:

This project is licensed under the [MIT License](https://spdx.org/licenses/MIT.html).

## Changelog :memo:

For a detailed list of changes, please refer to the [CHANGELOG](./CHANGELOG.md).

<!-- Refs -->
[author]: https://github.com/hasansezertasan
[pun]: https://github.com/hasansezertasan/pun
