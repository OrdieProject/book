Introduction
============

This book details the steps necessary to :term:`harden` a design from a soft FPGA to physical silicon.

Hardening Steps
---------------

In order to harden a design, generally the following steps are taken in order:

1. Validate the design works. If you're using Verilog, an FPGA can be helpful here. At the very least, use a simulator to ensure the design functions correctly.
2. Clone the Caravel project. Go to https://github.com/efabless/caravel_user_project/generate to do so.
3. Copy `openlane/user_proj_example` to your own project name, e.g. `openlane/my_project`
4. Modify the `config.json` in the new project:
  1.  Adjust `DESIGN_NAME` to reflect your top macro
  2.  Set `DIE_AREA` to the area of your project
  3.  Modify `VERILOG_FILES` to include the path to your topfile, as well as Verilog files -- wildcards are supported
  4.  Adjust `CLOCK_NET` and `CLOCK_PORT` to reflect the clock signals in your design
