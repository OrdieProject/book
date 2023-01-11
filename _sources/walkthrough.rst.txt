Walkthrough
-----------

1. Create a new Caravel user project from the template at https://github.com/efabless/caravel_user_project/
2. Clone the resulting project, and change to the resulting directory.
3. Add a .gitattributes file, if you like
4. Add an ``activate-caravel.sh`` script, and **be sure to run this script every time you want to work on the project**.
5. Run ``make setup`` to download the necessary files
6. If you have submodules, add them.
    1. Add Verilog code to verilog/rtl/
7. Rename ``openlane/user_proj_example`` to ``openlane/your_project_name``
8. Rename ``verilog/rtl/user_proj_example.v`` to ``verilog/rtl/your_project_name.v``
9. Modify ``verilog/rtl/your_project_name.v`` and add your custom Verilog.
10. Modify ``openlane/your_project_name/config.json``:
    1. Change ``DESIGN_NAME`` to match the top module inside ``your_project_name.v``
    2. Add all Verilog files to ``VERILOG_FILES``, including changing ``user_proj_example.v``. Wildcards are supported here.
    3. Modify ``CLOCK_NET`` and give it the net name of your clock(s)

activate-caravel.sh

.. code-block:: sh

   #!/bin/sh
   if [ "$0" = "activate-caravel.sh" ]
   then
      echo "Don't run $0, source it by running '. $0'"
      echo "Alternately, set the 'OPENLANE_ROOT', 'PDK_ROOT', and 'PDK' environment variables manually"
      exit 1
   fi

   export OPENLANE_ROOT=$(pwd)/dependencies/openlane_src
   export PDK_ROOT=$(pwd)/dependencies/pdks
   export PDK=sky130A

   # Note: these go outside of the project directory in order to help pass
   # precheck, which traverses the entire project directory looking for
   # violating files, including inside the ``dependencies`` directory.
   export PRECHECK_ROOT=$(realpath $(pwd)/..)/dependencies/precheck
   export CARAVEL_ROOT=$(realpath $(pwd)/..)/dependencies/caravel
   export MCW_ROOT=$(realpath $(pwd)/..)/dependencies/mgmt_core_wrapper
