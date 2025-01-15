FROM python:3.8-slim

WORKDIR ./app

ARG MINICONDA_VERSION=Miniconda3-latest-Linux-x86_64

RUN apt update && \
    apt install -y wget coreutils libgomp1 xorg --no-install-recommends && \
    apt clean

RUN wget https://repo.anaconda.com/miniconda/$MINICONDA_VERSION.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/miniconda && \
    rm /tmp/miniconda.sh

ENV PATH=/opt/miniconda/bin:$PATH

COPY ../../environment.yml .

RUN conda env create -f environment.yml

RUN conda init bash

RUN echo "source activate vbms" >> ~/.bashrc

ENV PATH=/opt/miniconda/envs/vbms/bin:$PATH

COPY . .

ENTRYPOINT ["/bin/bash", "--login", "-c"]

CMD ["python3 app.py"]
