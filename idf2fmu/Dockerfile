FROM nrel/energyplus:9.6.0

ENV DEBIAN_FRONTEND=noninteractive
ENV IDD_PATH="/EnergyPlus-9.6.0-4b123cf80f-Linux-Ubuntu20.04-x86_64/Energy+.idd" \
    IDF_PATH="/app/optimized.idf" \
    EPW_PATH="/app/PARIS_FR-hour.epw" \
    EnergyPlusToFMU_PATH="/app/EnergyPlusToFMU-v3.1.0/Scripts/EnergyPlusToFMU.py"

WORKDIR ./app

RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    g++ \
    libxml2-dev \
    python3.8 \
    python3.8-distutils \
    curl \
    tzdata \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.8 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["bash", "-c", "python3 $EnergyPlusToFMU_PATH -i $IDD_PATH -w $EPW_PATH -a 2 $IDF_PATH"]
