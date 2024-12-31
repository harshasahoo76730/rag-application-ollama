# ====================================================================================================
# Author:   Harsha Vardhan Sahoo
# Contact:  harshasahoo76730@gmail.com
# ====================================================================================================

FROM ubuntu:22.04

LABEL author="Harsha Vardhan Sahoo"
LABEL contact="harshasahoo76730@gmail.com"
LABEL description="RAG Development Environment"

USER root

SHELL ["/bin/bash", "-c"]

# Setup Bash Environment
RUN apt-get update -y && apt-get install -y apt-transport-https && \
    apt-get install -y -q --no-install-recommends gpg=\* gnupg=\* ca-certificates=\* wget=\* libtbb12=\* python3-pip=\* \
    gpg-agent software-properties-common wget curl git git-lfs jq vim make unzip p7zip-full gcc g++ meson dos2unix snapd \
    autoconf automake autogen cmake numactl lshw libtool libssl-dev libpython3-dev cpufrequtils tree network-manager && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup Python Environment
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip --default-timeout=1000 install --no-cache-dir --user \
    pypdf chromadb \
    langchain langchain_chroma langchain_ollama langchain_community && \
    ln -sf /usr/bin/python3 /usr/bin/python

ENV PATH="/root/.local/bin:${PATH}"

CMD ["/bin/bash", "-c"]
WORKDIR /home
