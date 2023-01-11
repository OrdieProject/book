Memory and Memories
===================

Memory is a subtle thing in chip design. Often when people hear the term "memory" they think of addressable, volatile storage. However memories can be far more than that.

In addition to the more traditional addressable RAM, memory can also be used to form caches, register files, or large buffers. It can also be used to form ROMs, in the case where memory is read-only.

Note that while it is sometimes possible to infer memory designs from Verilog code, there may be cases where the synthesizer fails to recognize a memory block and will instead turn it into a series of flip-flops. This can cause the synthesis duration to balloon to several times its ordinary duration, taking several hours instead of several minutes. Therefore it is recommended to use a :term:`blackbox` whenever possible.

OpenRAM
-------

`OpenRAM <https://github.com/VLSIDA/OpenRAM>`_ is currently the most efficient open source RAM compiler. It will create memory of an arbitrary width and depth and ensure the resulting design meets timing requirements.

.. note::
    Synthesizing OpenRAM blocks can take a long time -- several hours when doing :term:`LVS` extraction, so it is best to build your RAMs in a separate step before your main synthesis.

.. warning::
    OpenRAM has their own version of tools, as well as their own version of the PDK. OpenRAM does not support using the common set of tools or PDK. You **must** use their Docker image, as well as the PDK hosted by them.

OpenRAM memories are comparatively large and dense. The trade-off is that synthesizing them takes a long time.

DFFRAM
------

`DFFRAM <https://github.com/AUCOHL/DFFRAM>`_ is much faster to synthesize than OpenRAM, but results in lower density memories. DFFRAM can be used to synthesize small, oddly-shaped memories such as cache tag lines or register files.

Creating a new DFFRAM entity
----------------------------

1. Clone dffram: ``git clone https://github.com/AUCOHL/DFFRAM.git && cd DFFRAM``
2. Create a python venv: ``python -mvenv .; . bin/activate``
3. Install requirements: ``pip install -r requirements.txt``
4. Install volare: ``pip install volare``
5. List available PDKs: ``volare --pdk-root pdks ls-remote``
6. Install a PDK: ``volare enable --pdk-root pdks --pdk gf180mcu 3f9bdbd857564726b731760dc2c817e84ca7d8ac``
