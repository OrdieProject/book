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
        Hardware Definition Language. A language such as VHDL or Verilog that can be used to describe hardware. Produces :term:`RTL` when synthesized.

    RTL
        Register-Transfer Level. The logical circuit and state machine formed by synthesizing :term:`HDL`. RTL is sometimes referred to as :term:`IP`.

    Verilog
        A Hardware Definition Language that vaguely resembles Pascal.

    VHDL
        A Hardware Definition Language that vaguely resembles Ada.

    Yosys
        Yosys is a synthesis program which takes input such as Verilog code as well as primitives for a particular backend and generates outputs that can be fed into a tool for further processing. As an example, Yosys might turn a statement that adds two registers together into a series of ``LUT4`` adders that exist on a particular FPGA or PDK. Yosys will not do any sort of physical cell placement or routing, it will simply turn Verilog code into :term:`RTL`.

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

    CVC
        Circuit Validity Check. Ensures that the circuit does not have any errors such as signals crossing voltage domains, leaks due to intermittent floating inputs, or errors due to cutoff regions.

    Parasitic Extraction
        Parsitic Extraction involves creating an analogue model of the chip that can be used for simulation.

    SPEF
        Standard Parasitic Exchange Format. A file format that describes parasitics, and is the result of :term:`Parasitic Extraction`.

    LEC
        Logic Equivalency Check. This optional step ensures that the logic of the generated chip matches the original HDL. This step takes a very long time, and is usually omitted except for the final tapeout step.

    Volare
        A tool to manage installed PDKs, as well as a repository of prebuilt PDKs.

    harden
        The process of turning :term:`RTL` and other "soft" source design files into :term:`GDSII`. A hardware equivalent of "compiling".

    magic
        magic is a tool used to edit raw :term:`GDSII` files. It is also capable of running :term:`DRC` and antenna checks on the final product.

    DRC
        Design Rule Check. A :term:`PDK` has a number of design rules that indicate a wide number of rules such as minimum trace width, minimum spacing between two features, or minimum angle when routing edges. A DRC check ensures that the design meets these rules.

    LVS
        Layout Vs Schematic. This check ensures that the chip, as it was laid out, matches the schematic that did the layout. This step essentially reverse-engineers the chip and builds a netlist from the components it sees, then compares that netlist to the one that was used to generate the chip.

    signoff
        The process of verifying the resulting design meets the rules set forth by the :term:`PDK` and, when manufactured, will function as intended.