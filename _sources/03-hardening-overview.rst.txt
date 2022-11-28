Hardening Overview
==================

Now that all of the tools are installed, we can start working on the the actual process flow. The overall flow is described in `The OpenLane Overview <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/docs/source/flow_overview.md#openlane-architecture>`_ and describes the typical design sequence. Many of these steps are automated, though various steps may require additional inputs other than the outputs of their immediate predecessors.

Most tools are configured by adjusting environment variables, or by setting them in a `config.tcl` or `config.json` file. These tools also communicate by passing environment variables to child processes, and almost never pass project-specific settings on the command line.

Synthesis
---------

Synthesis is the process of taking :term:`HDL` and turning it into :term:`RTL`. This step is most familiar to those who have used FPGAs in the past, as it uses much the same tooling.

Yosys
^^^^^

The first step is to actually synthesize the :term:`RTL`. This is done by setting a number of environment variables, then running ``yosys`` and passing it the script `synth.tcl <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/scripts/yosys/synth.tcl>`_. This performs synthesis and generates a netlist file according to the ``SAVE_NETLIST`` environment variable.

.. code-block:: sh

    yosys -c $OPENLANE_ROOT/scripts/yosys/synth.tcl

OpenSTA
^^^^^^^

After the :term:`RTL` is synthesized, it must be analyzed to get a rough idea of what sort of timing we can expect from the finished product. Since we now know what sort of cells we have, this step can also tell us how much of the chip's area is being used. Finally, we can also know which nets form the "critical path" where the worst offenders are.

OpenSTA is bundled as part of ``OpenROAD``, and is invoked using the `sta.tcl <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/scripts/openroad/sta.tcl>`_ script from ``OpenLane``:

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/sta.tcl

Floorplanning
-------------

Floorplanning is the process of dividing the rectangular chip area into multiple zones and populating those zones with components that were synthesized.

Floorplanning is done over the course of several steps, with each step refining the previous one. These steps will attempt to fit the design :term:`core area`.

init_fp
^^^^^^^

This step takes the :term:`RTL` and places the cells in the specified area, ensuring that the cells all actually fit. It does this by dividing the area into rows and filling in components as it goes. This step also inserts any :term:`tie cell` that is required.

This reads ``merged.nom.lef`` and writes its output to the same file.

Note: It is currently unclear why this step is run twice.

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/floorplan.tcl
    openroad -exit $OPENLANE_ROOT/scripts/openroad/floorplan.tcl

ioplacer
^^^^^^^^

Every cell that was added has input and output pins. For example, if the synthesized :term:`RTL` contains an inverter, that inverter will have two pins.

The IO Placer step adds these pins to the design in random locations (?).

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/ioplacer.tcl

tapcell
^^^^^^^

The ``tapcell`` step inserts :term:`welltap` and :term:`endcap` cells into the design as necessary.

.. note::
    The log output uses the term :term:`decap` here, but it seems as though it's actually inserting :term:`endcap` cells instead. Is this a typo?

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/tapcell.tcl

pdngen
^^^^^^

The final :term:`floorplan` step is to generate the power distribution network. This is accomplished with the ``pdngen`` tool from ``openroad``.

This tool creates the power net for the chip. It is driven by evaluating `pdn_cfg.tcl <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/scripts/openroad/common/pdn_cfg.tcl>`_ to define the networks prior to running ``pdn.tcl``

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/pdn.tcl

Placement
---------

Placement is the process of selecting where to put elements in a design. There are two placement strategies available: Random, or ``RePlAce``. Random placement is fast but not very efficient, though is fine for simple designs.

The ``PL_RANDOM_GLB_PLACEMENT`` setting in ``config.json`` or ``config.tcl`` can be set to ``true`` to use random placement or ``false`` to use ``RePlAce``.

random_global_placement
^^^^^^^^^^^^^^^^^^^^^^^

This uses a Python script to randomly place cells in a design. For simple designs, this can be faster than using ``RePlAce``. It's a `very simple script <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/scripts/odbpy/random_place.py>`_ and doesn't get invoked using the normal TCL flow.

global_placement_or
^^^^^^^^^^^^^^^^^^^

This command is aliased to ``global_placement``.

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/gpl.tcl

Placement Resizer
^^^^^^^^^^^^^^^^^

The Placement Resizer performs several sub-steps, including estimating parasitics and running static timing analysis again.

The bulk of the step is ``detailed_placement`` which shuffles cells that have just been placed in order to ensure they're in legal positions.

If ``PL_RESIZER_DESIGN_OPTIMIZATIONS`` is true, then the placement resizer step is run, otherwise it is skipped.

Clock Tree Synthesis
--------------------

The next step is to synthesize the clock distribution network. If ``CLOCK_PORT`` and ``CLOCK_NET`` are not set, then this step is skipped.

cts
^^^

This uses ``TritonCTS``, which is built into OpenROAD.

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/cts.tcl

Routing
-------

3. **Routing**
    1. `FastRoute` - Performs global routing to generate a guide file for the detailed router
    2. `TritonRoute` - Performs detailed routing
    3. `OpenRCX` - Performs SPEF extraction
4. **Tapeout**
    1. `Magic` - Streams out the final GDSII layout file from the routed def
    2. `KLayout` - Streams out the final GDSII layout file from the routed def as a back-up
5. **Signoff**
    1. `Magic` - Performs DRC Checks & Antenna Checks
    2. `KLayout` - Performs DRC Checks
    3. `Netgen` - Performs LVS Checks
    4. `CVC` - Performs Circuit Validity Checks

Running the hardening flow
==========================

You can tie everything together by running ``flow.tcl`` from ``OpenLane``:

.. code-block:: sh

    PYTHONPATH=$VIRTUAL_ENV/lib/python3.10/site-packages/ \
    STD_CELL_LIBRARY_OPT=sky130_fd_sc_hd \
    STD_CELL_LIBRARY=sky130_fd_sc_hd \
    PDK_ROOT=/opt/Si/PDKs/share/pdk \
    PDK=sky130B \
    ./flow.tcl \
    -design /opt/Si/work/inverter/ \
    -ignore_mismatches