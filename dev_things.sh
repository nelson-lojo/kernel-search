
prep_conda() {
    pip install gdown
    gdown 1xtqmAVYeISAmicPC0QA753MZ8Z4M2ttA
    mv conda.zip /workspaces/project/chipyard/
    
    if [[ -d /workspaces/project/chipyard/.conda-env ]]; then return 0; fi
    cd /workspaces/project/chipyard/ && unzip conda.zip
}
