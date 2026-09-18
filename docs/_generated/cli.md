# `pun`

**Usage**:

```console
$ pun [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `version`: Show the current version number of pun.
* `info`: Display information about the pun...
* `interactive`: Start interactive mode (TUI) for pun.

## `pun version`

Show the current version number of pun.

Show the version number:
    pun version

Example output:
    0.1.0

Raises:
    typer.Exit: If the package metadata cannot be found.

**Usage**:

```console
$ pun version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `pun info`

Display information about the pun application.

Show application information:
    pun info

Example output:
    Application Version: 0.1.0
    Python Version: 3.12.0 (CPython)
    Platform: Darwin

Raises:
    typer.Exit: If the package metadata cannot be found.

**Usage**:

```console
$ pun info [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `pun interactive`

Start interactive mode (TUI) for pun.

Launch the terminal user interface:
    pun interactive

Raises:
    typer.Exit: Propagating the TUI&#x27;s exit code.

**Usage**:

```console
$ pun interactive [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
