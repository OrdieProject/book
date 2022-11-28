Memory and Memories
===================

Memory is a subtle thing in chip design. Often when people hear the term "memory" they think of addressable, volatile storage. However memories can be far more than that.

In addition to the more traditional addressable RAM, memory can also be used to form caches, register files, or large buffers. It can also be used to form ROMs, in the case where memory is read-only.

OpenRAM
-------

`OpenRAM <https://github.com/VLSIDA/OpenRAM>`_ is currently the most efficient open source RAM compiler. It will create memory of an arbitrary width and depth and ensure the resulting design meets timing requirements.

.. note::
    Synthesizing OpenRAM blocks can take a long time -- several hours when doing :term:`LVS` extraction, so it is best to build your RAMs in a separate step before your main synthesis.

.. warning::
    OpenRAM has their own version of tools, as well as their own version of the PDK. OpenRAM does not support using the common set of tools or PDK. You **must** use their Docker image, as well as the PDK hosted by them.

OpenRAM memories are comparatively large and dense. The tradeoff is that synthesizing them takes a long time.

DFFRAM
------

`DFFRAM <https://github.com/AUCOHL/DFFRAM>`_ is much faster to synthesize than OpenRAM, but results in lower density memories. DFFRAM can be used to synthesize small, oddly-shaped memories such as cache tag lines or register files.