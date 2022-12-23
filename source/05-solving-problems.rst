Solving Common Problems
=======================

There are a number of common pitfalls when hardening a design. Their solutions are not always the most intuitive, however with a little deductive reasoning you can solve problems.

**Have a look at the design in the OpenRoad GUI**. If you have OpenRoad installed, run ``openroad -gui`` and load the offending ``.odb`` file.  This can be accomplished using the ``read_db`` command, or by selecting ``Open DB`` from the ``File`` menu. The offending file can be found in ``openlane/$DESIGN/runs/$RUN/tmp/$STEP/*.odb``.

Synthesis Takes a Very Long Time
--------------------------------

If your synthesis process takes a very long time, you may need to simplify your design. Depending on the design, this may be either easy or difficult.

* **Avoid using large memories**. While the synthesizer is capable of synthesizing memories from Verilog, this is profoundly inefficient and can take a long time. Instead, prefer to use blackbox memories from either ``OpenRam`` or ``DFFRAM``.
* **Use blackbox sub-designs**. If it takes a long time to place and route the entire design, you can break it up into multiple sub-projects. That way, your top project consists of just a single project with multiple holes in it, allowing you to pre-synthesize (and pre-place and pre-route) chunks of your project.

Unable to Place Design
----------------------

OpenLane may be unable to place elements into your design if it contains a lot of elements in a small amount of space.

Placement involves roughly scattering elements around, then shuffling them into place so that they don't overlap while common elements stay close together.

If the placement step fails, try the following:

* **Increase the die area** -- The die area is set by both the ``DIE_AREA`` and the ``FP_SIZING`` configuration variables. The die area for MPW runs is ``2.92mm x 3.52mm``, so the maximum size available here is ``0 0 2920 3520`` when ``FP_SIZING`` is set to ``absolute``.
* **Increase placement density** -- The placer will add space between cells in order to run wires and buffers. Increase ``FP_CORE_UTIL`` and ``PL_TARGET_DENSITY`` in order to reduce this space. These values are percentages, and should be between 20% and 70%. ``PL_TARGET_DENSITY`` goes from ``0.00`` to ``1.00``, and ``FP_CORE_UTIL`` goes from ``0`` to ``100``. Ordinarily you should set ``FP_CORE_UTIL`` to be 5% more than ``PL_TARGET_DENSITY``.
* **Change placement strategy** -- If you're having trouble routing elements, you can try changing the placement strategy to reduce the number of elements that need to be placed. Use ``-synth_explore`` (TODO: write how to invoke this) in order to find a more efficient placement strategy, then set the ``SYNTH_STRATEGY`` variable.  An example strategy might be ``AREA 2``.

Unable to Route Design
----------------------

If OpenLane is unable to route the design, it means that it cannot fit enough wires between the cells in order to connect various instances together.

The solution is to relax density, allowing more space for wires.

* **Decrease placement density** -- If elements are too close together, the router may not be able to add wires to your design. Reduce the placement density by lowering ``PL_TARGET_DENSITY`` and ``FP_CORE_UTIL``. Note that this is in direct opposition to placement, so the goal is to find a sweet spot where the design can place and also route.
* **Reduce bus widths** -- If you have very wide buses, this requires routing many signals in parallel, which increases density in parts of the design.

Setup Violation
---------------

A Setup Violation generally means that the design successfully placed and routed, but the design would not meet timing at the given frequency.

* **Lower the frequency**. You can increase the ``CLOCK_PERIOD`` to space clocks further apart, resulting in a lower frequency.
