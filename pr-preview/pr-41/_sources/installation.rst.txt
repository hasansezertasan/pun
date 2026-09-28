Installation
============

``pun`` is an end-user application, not a library, so install
it as a standalone tool rather than as a project dependency. Its primary entry
point is the ``pun`` command.

Stable release
--------------

Install ``pun`` into an isolated environment with your
preferred tool installer:

.. code-block:: sh

   uv tool install pun

.. code-block:: sh

   pipx install pun

Or run it without installing:

.. code-block:: sh

   uvx pun

From source
-----------

The source files for ``pun`` can be downloaded from the
`GitHub repo <https://github.com/hasansezertasan/pun>`_.

You can either clone the public repository:

.. code-block:: sh

   git clone https://github.com/hasansezertasan/pun.git

Or download the
`tarball <https://github.com/hasansezertasan/pun/tarball/main>`_:

.. code-block:: sh

   mkdir pun
   curl -fL https://github.com/hasansezertasan/pun/tarball/main | tar -xz --strip-components=1 -C pun

Once you have a copy of the source, you can install it with:

.. code-block:: sh

   cd pun
   uv tool install .
