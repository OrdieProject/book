Prerequisites
=============

A large number of tools are required in order to :term:`harden` a design. Each tool performs a very specific task, and most tools are required in order to complete a full flow.

We also need a :term:`PDK`, which is akin to a standard library in a programming language that also defines limits as to what our design can do, such as how small features can be and how quickly transistors can switch.

Creating a Python venv
======================

Python dependencies become much easier to manage if you install them into a ``venv``. This keeps them separate on a per-project basis. It is recommended to set up a ``venv`` for these tools and to ``activate`` it prior to installing or using any of these tools.

You can set an environment variable ``OPEN_SI_PREFIX`` to point to where you want everything to be installed.

.. code-block:: sh

    $ python3 -mvenv $OPEN_SI_PREFIX
    $ . $OPEN_SI_PREFIX/bin/activate
    ($OPEN_SI_PREFIX) $

You can look in the ``bin/`` directory to run a different activation script if you run a non-Bourne shell. On Windows, the directory will be called ``Scripts/``, although installing these tools is currently unsupported on Windows.

You will need to run the ``activate`` step prior to doing any steps presented here, and you will know you're in the venv because your command prompt will have the venv name printed before it.

Installing Required Software
============================

There are many different software components that are required in order to :term:`harden` a chip. This section covers each piece of software and how to install it.

Magic
-----

Magic is a chip layout and design tool. It is used by many steps in the flow to manipulate physical aspects of the final chip.

1. Clone ``magic`` and compile it.

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/magic.git
    cd magic
    ./configure --prefix=$OPEN_SI_PREFIX
    make
    make install

Ensure that the prefix is added to the path.

OpenROAD
--------

OpenROAD contains multiple tools within it. It is a general orchestrator for various hardening commands. This includes floorplanning, placement, clock generation and optimization, global and detailed routing, and final :term:`GDSII` generation.

1. Clone the repository

.. code-block:: sh

    git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD.git
    cd OpenROAD

2. Install dependencies

Dependencies only work on CentOS, Ubuntu, and Mac. **Note that this will install development dependencies to `/usr/local`**


.. code-block:: sh

    sudo ./etc/DependencyInstaller.sh -dev

3. Compile the project

You can specify a different directory here. This will compile a "release" build by default, but you can specify ``-DCMAKE_BUILD_TYPE=Debug`` in order to compile a debug version. You can also specify ``-DGPU=true`` in order to enable gpu support.

.. code-block:: sh

    mkdir build
    cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=$OPEN_SI_PREFIX
    make
    make install

OpenLane
--------

OpenLane is a set of scripts that drive the other tools. It is the primary interface that will be used when running the design flow.

1. Clone the project

.. code-block:: sh

    git clone https://github.com/The-OpenROAD-Project/OpenLane.git
    cd OpenLane

2. Install Python dependencies

If you're using a python environment, activate it before running this command:

.. code-block:: sh

    pip install \
        -r dependencies/python/run_time.txt \
        -r dependencies/python/compile_time.txt \
        -r dependencies/python/precompile_time.txt

Yosys
-----

Yosys is used to synthesize logic from Verilog source code.

.. code-block:: sh

    git clone https://github.com/YosysHQ/yosys.git
    cd yosys
    make config-gcc
    make
    make install PREFIX=$OPEN_SI_PREFIX

KLayout
-------

Klayout is used to generate :term:`GDSII` as an alternative to :term:`magic`. It is also used to perform :term:`DRC` checks as part of :term:`signoff`.

1. Install dependencies. This varies depending on your platform.

.. code-block:: sh

    sudo apt install   gcc g++ make   qttools5-dev libqt5xmlpatterns5-dev qtmultimedia5-dev libqt5multimediawidgets5 libqt5svg5-dev   ruby ruby-dev   python3 python3-dev   libz-dev

2. Clone and compile the program. Note that you can add `-option -j4` to e.g. build with 4 threads.

.. code-block:: sh

    git clone https://github.com/KLayout/klayout.git
    cd klayout
    ./build.sh -prefix $OPEN_SI_PREFIX

netgen
------

Netgen is used to generate a netlist from the resulting chip in order to perform :term:`LVS` checks.

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/netgen.git
    cd netgen
    ./configure --prefix=$OPEN_SI_PREFIX
    make
    make install

Circuit Validity Checker
------------------------

The Circuit Validity Checker is used towards the end of the hardening process to ensure that the final circuit matches the requirements.

.. code-block:: sh

    sudo apt install bison automake autopoint
    git clone https://github.com/d-m-bailey/cvc.git
    cd cvc
    autoreconf -vif
    ./configure --disable-nls --prefix=$OPEN_SI_PREFIX
    make
    make install

OpenRAM
=======

You may need custom memory sizes, for example if you're working on tagged cache memory. In this case, you will need to compile memories yourself.

.. code-block:: sh

    git clone https://github.com/VLSIDA/OpenRAM.git
    cd OpenRAM
    pip install -r requirements.txt

Additionally, OpenRAM requires its own copy of the PDKs. 

.. note::

    OpenRAM requires its own, pinned copy of the PDK. It is NOT able to use another version of the PDK you may have. Doing so will cause strange breakage such as ``Could not find pin gnd on col_cap_bitcell_2port``, or generation never actually finishing.

:term:`PDK`
===========

The PDK you select will depend on what process you want to target. While it is possible to port designs between processes, you may run into issues if you rely on features that are not present in the new node. This is similar to trying to port code from one operating system to another -- if you rely on fancy features, you will need to work harder to find an equivalent in the new process.

There are two options available when installing a PDK: Prebuilt, and build-it-yourself.

Prebuilt :term:`PDK`
--------------------

You can use a tool called :term:`volare` to download prebuilt open PDKs. Volare is both a PDK manager and a PDK repository. You can install volare from pip using ``python3 -m pip install -U volare``, and more documentation is available `in its README <https://github.com/efabless/volare#usage>`_.

Assemble the PDK
----------------

The PDK comes as disparate components that must be checked out. It is not distributed as a monolithic binary. Each PDK is bespoke, and requires a setup step in order to assemble into a format that can be used by the OpenROAD project.

A tool called `open_pdks <https://github.com/RTimothyEdwards/open_pdks/>`_ is used to do the assembly. This should be run on a Linux machine. You will also need ``magic``, which is used to process the GDS files that are generated  during the process.

1. Install ``python3 git m4 tcsh tcl-dev tk-dev`` as well as a C compiler.

2. Clone ``open_pdks``

.. code-block:: sh

    git clone https://github.com/RTimothyEdwards/open_pdks.git
    cd open_pdks

3. Configure the PDKs you want installed as well path you want to install files to:

.. code-block:: sh

    ./configure \
        --enable-sky130-pdk \
        --enable-sram-sky130 \
        --enable-gf180mcu-pdk \
        --prefix=/opt/Si/PDKs/


4. Download the files and process them. This can take a while because it also installs a Python environment in order to do some of the processing.

.. code-block:: sh

    make

5. Install the PDK files

.. code-block:: sh

    make install
