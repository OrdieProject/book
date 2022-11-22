Glossary
========

This page describes terms that are used in the Ordie project, as well as in open silicon and IC design.

.. glossary:: 

    The OpenROAD Project
      OpenROAD is the umbrella project that brings together various open silicon tools and projects to go from RTL to GDS.

    openroad
        A product produced by the OpenROAD project that incorporates floorplanning, placement, cts, optimization, and global routing. Used as part of the OpenLane flow.

    OpenLane
        A full, end-to-end set of scripts that can be used to generate GDSII files from HDL. OpenLane is the entire "toolchain" that bundles all other projects together and supports running them in sequence. OpenLane consists of TCL and Python scripts that glue all of the other projects together.

    HDL
        Hardware Definition Language. A language such as VHDL or Verilog that can be used to describe hardware.

    Verilog
        A Hardware Definition Language that vaguely resembles Pascal.

    Yosys
        Yosys is a synthesis program which takes input such as Verilog code as well as primitives for a particular backend and generates outputs that can be fed into a tool for further processing. As an example, Yosys might turn a statement that adds two registers together into a series of `LUT4` adders that exist on a particular FPGA or PDK. Yosys will not do any sort of physical cell placement or routing, it will simply turn Verilog code into hardware primitives.

    PDK
        Process Design Kit. The set of primitives and design rules available on a certain foundary's process node. A PDK may include basics such as NAND and NOR gates, transistors, FETs, capacitors, and resistors, and it may include more advanced cells such as RAMs and fuses.

    GDSII
        Also called GDS2 or simply GDS, this is the de-facto industry standard for submitting chip designs. It can be thought of as the "Gerber" equivalent for chips. Note that GDSII supports "black boxes" where the foundary is directed to add their own IP blocks.

    IP
        The industry term for an existing design, originally standing for "Intellectual Property". An IP core can be thought of as a library that is added to a chip design. For example, you may add I2C IP in order to allow your design to communicate using that bus.

    STA
        Static Timing Analysis. This step in the synthesis flow determines how fast a circuit can run, and whether it can meet the frequency required by the designer.

    DFT
        Design For Testing. This step adds features to the chip that can be used for diagnostics, such as scan chain insertion. This allows for the designer to probe various sections of the chip once it has been built.

    Floorplan
        An initial arrangement of various sections on the chip. Floorplans are rough guides that are used to plan the rest of layout. For example, bond pads may be placed at the edges early on in the floorplanning process.

    Placement
        Placement involves assigning cells their physical (X, Y) coordinates. Placement does not do any routing.

    CTS
        Clock Tree Synthesis. This runs wires for the clock tree, adds buffers as necessary, and tries to keep latency and skew within acceptable parameters. This step comes immediately after the placement step, because clock resources are so important to keeping the chip synchronized.

    Parasitic Extraction
        Parsitic Extraction involves creating an analogue model of the chip that can be used for simulation.

    LEC
        Logic Equivalency Check. This optional step ensures that the logic of the generated chip matches the original HDL. This step takes a very long time, and is usually omitted except for the final tapeout step.
