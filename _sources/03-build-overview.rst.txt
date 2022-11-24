Build Overview
==============

Now that all of the tools are installed, we can start working on the the actual process flow. The overall flow is described in `The OpenLane Overview <https://github.com/The-OpenROAD-Project/OpenLane/blob/master/docs/source/flow_overview.md#openlane-architecture>`_ and describes the typical design sequence. Many of these steps are automated, though various steps may require additional inputs other than the outputs of their immediate predecessors.

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

Note: It is currently unclear why this step is run twice.

.. code-block:: sh

    openroad -exit $OPENLANE_ROOT/scripts/openroad/floorplan.tcl
    openroad -exit $OPENLANE_ROOT/scripts/openroad/floorplan.tcl

ioplacer
^^^^^^^^

2. **Floorplaning**
    2. `ioplacer` - Places the macro input and output ports
    3. `pdngen` - Generates the power distribution network
    4. `tapcell` - Inserts welltap and decap cells in the floorplan
3. **Placement**
    1. `RePLace` - Performs global placement
    2. `Resizer` - Performs optional optimizations on the design
    3. `OpenDP` - Performs detailed placement to legalize the globally placed components
4. **CTS**
    1. `TritonCTS` - Synthesizes the clock distribution network (the clock tree)
5. **Routing**
    1. `FastRoute` - Performs global routing to generate a guide file for the detailed router
    2. `TritonRoute` - Performs detailed routing
    3. `OpenRCX` - Performs SPEF extraction
6. **Tapeout**
    1. `Magic` - Streams out the final GDSII layout file from the routed def
    2. `KLayout` - Streams out the final GDSII layout file from the routed def as a back-up
7. **Signoff**
    1. `Magic` - Performs DRC Checks & Antenna Checks
    2. `KLayout` - Performs DRC Checks
    3. `Netgen` - Performs LVS Checks
    4. `CVC` - Performs Circuit Validity Checks
