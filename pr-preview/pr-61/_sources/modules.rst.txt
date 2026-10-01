.. A 7-character "=" underline (the length of "Modules") is treated as a
   merge-conflict separator by ``git diff --check`` / ``check-merge-conflict``;
   keep this underline longer than the title to avoid the false positive.

Modules
=========

An overview of the packages that make up ``pun``.
The API reference below is generated automatically from the source docstrings.

Core (``pun.core``)
---------------------------

Always-included infrastructure.

.. automodule:: pun.core.config

.. automodule:: pun.core.dirs

.. automodule:: pun.core.logging_setup

Utilities (``pun.utils``)
---------------------------

Shared helper functions.

.. automodule:: pun.utils

CLI (``pun.cli``)
---------------------------

Typer command-line interface exposing ``version`` and ``info`` commands.

.. automodule:: pun.cli.app

TUI (``pun.tui``)
---------------------------

Textual terminal user interface.

.. automodule:: pun.tui.app


.. TODO @hasansezertasan: Document your own modules here as the project grows.
