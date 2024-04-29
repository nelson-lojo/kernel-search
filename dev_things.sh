
prep_conda() {
    pip install gdown
    gdown 1xtqmAVYeISAmicPC0QA753MZ8Z4M2ttA
    mv conda.zip chipyard/
    cd chipyard/ && unzip conda.zip
}
