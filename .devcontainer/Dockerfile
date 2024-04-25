FROM mcr.microsoft.com/devcontainers/universal 

# RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
# RUN bash Miniforge3-Linux-x86_64.sh -y
# RUN conda init
RUN apt update -y && apt install kmod -y

RUN conda install -n base python==3.10 -y

RUN conda install -n base conda-libmamba-solver -y
RUN conda config --set solver libmamba

RUN conda install -n base conda-lock==1.4.0 -y

CMD bash
