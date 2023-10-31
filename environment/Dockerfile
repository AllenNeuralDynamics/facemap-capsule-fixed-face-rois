# hash:sha256:b483f637511fce8db9503838ce623d44e52da275561cb43b49cdfcfca9637e7d
FROM registry.codeocean.allenneuraldynamics.org/codeocean/tensorflow:2.11-python3.10-cuda11.7.0-runtime-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ffmpeg=7:4.4.2-0ubuntu0.22.04.1 \
        libcublas-12-0=12.0.2.224-1 \
        libcudnn8=8.9.5.29-1+cuda12.2 \
        libegl1-mesa=23.0.4-0ubuntu1~22.04.1 \
        libsm6=2:1.2.3-1build2 \
        libxext6=2:1.3.4-1build1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U --no-cache-dir \
    facemap[gui]==1.0.4 \
    h5py==3.10.0 \
    matplotlib==3.8.0 \
    natsort==8.4.0 \
    numba==0.58.1 \
    numpy==1.26.1 \
    opencv-python-headless==4.8.1.78 \
    pyqt6==6.5.3 \
    pyqtgraph==0.13.3 \
    qtpy==2.4.1 \
    scikit-learn==1.3.2 \
    scipy==1.11.3 \
    torch==2.1.0 \
    tqdm==4.66.1 \
    umap-learn==0.5.4

COPY postInstall /
RUN /postInstall
