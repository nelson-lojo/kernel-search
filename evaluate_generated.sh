#!/bin/bash

PROJ_ROOT=/workspaces/project/
CHIPYARD=$PROJ_ROOT/chipyard
GEMMINI=$CHIPYARD/generators/gemmini/
GEMMINI_TESTS=$GEMMINI/software/gemmini-rocc-tests/
C_TESTS=$GEMMINI_TESTS/bareMetalC/

generate_exo() {
    # exocc -o generated_c --stem generated_ker out.py
    cat $C_TESTS/generated_harness_base.c > $C_TESTS/generated_harness.c
    cat generated_c/generated_ker.c | tail -n+7 >> $C_TESTS/generated_harness.c
}

build_and_run() {
    MY_TMP_DIR=`pwd`
    cd $GEMMINI_TESTS && ./build.sh -s &> /dev/null
    # cd $GEMMINI && ./scripts/run-spike.sh generated_harness
    spike --extension=gemmini -l --log=$PROJ_ROOT/log $GEMMINI_TESTS/build/bareMetalC/generated_harness-baremetal
    cd $MY_TMP_DIR
}

generate_exo
build_and_run

cd $PROJ_ROOT

