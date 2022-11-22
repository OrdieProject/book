Design Sequence
===============

The following steps are performed when synthesizing a design:

1. Synthesis

Checkout Notes
--------------

1. Create a `config.json` next to the design
2. Check out the PDK

Assemble the PDK
----------------

The PDK comes as disparate components that must be checked out. It is not distributed as a monolithic binary. Each PDK is bespoke, and requires a setup step in order to assemble into a format that can be used by the OpenROAD project.

A tool called [open_pdks](https://github.com/RTimothyEdwards/open_pdks/) is used to do the assembly. This should be run on a Linux machine. You will also need `magic`, which is used to process the GDS files that are generated  during the process.

1. Install `python3 git m4 tcsh tcl-dev tk-dev` as well as a compiler.

2. Clone `magic` and compile it.

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/magic.git
    cd magic
    ./configure --prefix=[your prefix]
    make
    make install

Ensure that the prefix is added to the path.

3. Clone `open_pdks`

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/open_pdks.git
    cd open_pdks

4. Configure the PDKs you want installed as well path you want to install files to:

.. code-block:: sh

    ./configure \
        --enable-sky130-pdk \
        --enable-gf180mcu-pdk \
        --prefix=/opt/Si/PDKs/


5. Download the files and process them. This can take a while because it also installs a Python environment in order to do some of the processing.

.. code-block:: sh

    make

6. Install the PDK files

.. code-block:: sh

    make install

Build OpenROAD
--------------

OpenROAD contains multiple tools within it. It is a general orchestrator for various build commands. This includes floorplanning, placement, clock generation and optimization, global and detailed routing, and final GDSII generation.

1. Clone the repository

.. code-block:: sh

    git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD.git
    cd OpenROAD

2. Install dependencies

Dependencies only work on CentOS, Ubuntu, and Mac.


.. code-block:: sh

    sudo ./etc/DependencyInstaller.sh -dev

3. Compile the project

You can specify a different directory here. This will build a "release" build by default, but you can specify `-DCMAKE_BUILD_TYPE=Debug` in order to build a debug version. You can also specify `-DGPU=true` in order to enable gpu support.

.. code-block:: sh

    mkdir build
    cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=[path]
    make
    make install

Install OpenLane
----------------

OpenLane is a set of scripts that drive the other tools.

1. Clone the project

.. code-block:: sh

    git clone https://github.com/The-OpenROAD-Project/OpenLane.git
    cd OpenLane

2. Install Python dependencies

If you're using a python environment, activate it before running this command:

.. code-block:: sh

    pip install -r dependencies/python/run_time.txt  -r dependencies/python/compile_time.txt -r dependencies/python/precompile_time.txt

Install Yosys
-------------

Yosys is used to synthesize logic from Verilog source code

.. code-block:: sh

    git clone https://github.com/YosysHQ/yosys.git
    cd yosys
    make config-gcc
    make
    make install PREFIX=[path]

Install klayout
---------------

Klayout is used to generate GDSII. It's not clear why klayout is used and not magic.

1. Install dependencies. This varies depending on your platform.

.. code-block:: sh

    sudo apt install   gcc g++ make   qttools5-dev libqt5xmlpatterns5-dev qtmultimedia5-dev libqt5multimediawidgets5 libqt5svg5-dev   ruby ruby-dev   python3 python3-dev   libz-dev

.. code-block:: sh

    git clone https://github.com/KLayout/klayout.git
    cd klayout
    ./build.sh -prefix [path]

Install netgen
--------------

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/netgen.git
    cd netgen
    ./configure --prefix=[path]
    make
    make install

Install cvc_rv
--------------

.. code-block:: sh

    sudo apt install bison automake autopoint
    git clone https://github.com/d-m-bailey/cvc.git
    cd cvc
    autoreconf -vif
    ./configure --disable-nls --prefix=[path]
    make
    make install

Run the build
=============

.. code-block:: sh

    PYTHONPATH=$VIRTUAL_ENV/lib/python3.10/site-packages/ \
    STD_CELL_LIBRARY_OPT=sky130_fd_sc_hd \
    STD_CELL_LIBRARY=sky130_fd_sc_hd \
    PDK_ROOT=/opt/Si/PDKs/share/pdk \
    PDK=sky130B \
    ./flow.tcl \
    -design /opt/Si/work/inverter/ \
    -ignore_mismatches