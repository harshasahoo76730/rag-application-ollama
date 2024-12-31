# ====================================================================================================
# Author:   Harsha Vardhan Sahoo
# Contact:  harshasahoo76730@gmail.com
# Description: RAG Environment using Ollama
# ====================================================================================================

FROM ubuntu:22.04

USER root

SHELL ["/bin/bash", "-c"]

# Setup Bash Environment
RUN apt-get update -y && apt-get install -y apt-transport-https && \
    apt-get install -y -q --no-install-recommends gpg=\* gnupg=\* ca-certificates=\* wget=\* curl=\* python3-pip=\* \
    software-properties-common autoconf autogen automake cmake make meson git git-lfs gcc g++ jq vim unzip p7zip-full \
    snapd dos2unix lshw numactl cpufrequtils network-manager tree libtool libssl-dev libpython3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup Python Environment
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip --default-timeout=1000 install --no-cache-dir --upgrade --user \
    pypdf pycryptodomex cryptography chromadb \
    langchain langchain_chroma langchain_ollama langchain_community && \
    ln -sf /usr/bin/python3 /usr/bin/python

ENV PATH="/root/.local/bin:${PATH}"

CMD ["/bin/bash", "-c"]
