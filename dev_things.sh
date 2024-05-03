
prep_conda() {
    pip install gdown

    if [[ ! -f /workspaces/project/chipyard/conda.zip ]]; then 
        gdown 1xtqmAVYeISAmicPC0QA753MZ8Z4M2ttA
        mv conda.zip /workspaces/project/chipyard/
    fi
    
    if [[ -d /workspaces/project/chipyard/.conda-env ]]; then return 0; fi
    cd /workspaces/project/chipyard/ && unzip conda.zip
}
