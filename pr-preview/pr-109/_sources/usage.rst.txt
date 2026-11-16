Usage
=====

As a library
------------

Look up the installed distribution version:

.. literalinclude:: examples/version_lookup.py
   :language: python
   :caption: examples/version_lookup.py

For short interactive snippets embedded in prose, the ``docs-doctest`` task
executes ``>>>`` blocks too:

.. doctest::

   >>> from pun.__metadata__ import PROJECT_NAME
   >>> PROJECT_NAME
   'pun'

As a command-line tool
----------------------

To use ``pun`` as a command-line tool:

.. code-block:: sh

   pun version
   pun info

Or invoke it programmatically from Python:

.. literalinclude:: examples/cli_usage.py
   :language: python
   :caption: examples/cli_usage.py

As a TUI
--------

To launch the terminal user interface:

.. code-block:: sh

   pun interactive

Retrieve the info message without starting the TUI:

.. literalinclude:: examples/tui_usage.py
   :language: python
   :caption: examples/tui_usage.py
