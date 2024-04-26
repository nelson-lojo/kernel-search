#!/bin/bash

PROJ_ROOT=/workspaces/project/
CHIPYARD=$PROJ_ROOT/chipyard
GEMMINI=$CHIPYARD/generators/gemmini/
GEMMINI_TESTS=$GEMMINI/software/gemmini-rocc-tests/
C_TESTS=$GEMMINI_TESTS/bareMetalC/

install_docker() {
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    
    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

    # sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
}

install_llama3() {
    huggingface-cli login
    huggingface-cli download meta-llama/Meta-Llama-3-8B --include "original/*" --local-dir Meta-Llama-3-8B
}

generate_exo() {
    exocc -o generated_c --stem generated_ker out.py
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

# install_miniconda() {
#     mkdir -p ~/miniconda3
#     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
#     bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
#     rm -rf ~/miniconda3/miniconda.sh
#     ~/miniconda3/bin/conda init bash
    
#     bash
# }

# install_conda_pkgs() {
#     sudo apt update -y && sudo apt install kmod -y
#     conda install -n base python==3.10 -y

#     conda install -n base conda-libmamba-solver -y
#     conda config --set solver libmamba
    
#     conda install -n base conda-lock==1.4.0 -y
# }

generate_exo
build_and_run

cd $PROJ_ROOT
# install_miniconda
