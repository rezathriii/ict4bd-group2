FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && \
    apt install -y unzip g++ libgomp1 libxml2 libxml2-dev \
    build-essential cmake pkg-config wget sudo \
    libx11-6 libxrender1 libxtst6 software-properties-common && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.8 python3.8-distutils && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN wget "https://github.com/NREL/EnergyPlus/releases/download/v9.6.0/EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu20.04-x86_64.sh" && \
    chmod +x EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu20.04-x86_64.sh && \
    echo "y" | bash EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu20.04-x86_64.sh --silent --prefix=/usr/local/EnergyPlus-9-6-0 && \
    rm EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu20.04-x86_64.sh

RUN echo 'export PATH="/usr/local/EnergyPlus-9-6-0:$PATH"' >> /etc/environment && \
    echo 'export PATH="/usr/local/EnergyPlus-9-6-0:$PATH"' > /etc/profile.d/energyplus.sh && \
    ln -s /usr/local/EnergyPlus-9-6-0/energyplus /usr/bin/energyplus

WORKDIR /app

ENV ENERGYPLUSTOFMU_PATH="/app/EnergyPlusToFMU/Scripts/EnergyPlusToFMU.py"
ENV ENERGYPLUS_PATH="/usr/local/EnergyPlus-9-6-0/Energy+.idd"
ENV EPW_PATH="/shared/org/weather.epw"
ENV IDF_PATH="/shared/org/opt_model.idf"

RUN wget "https://github.com/lbl-srg/EnergyplusToFMU/releases/download/v3.1.0/EnergyPlusToFMU-v3.1.0.zip" && \
    mkdir -p EnergyPlusToFMU && \
    unzip EnergyPlusToFMU-v3.1.0.zip -d EnergyPlusToFMU && \
    rm -f EnergyPlusToFMU-v3.1.0.zip

CMD ["bash", "-c", "mkdir -p /shared/logs; \
     echo 'EnergyPlusToFMU has started...'; \
     cd /shared/fmu && python3 \"${ENERGYPLUSTOFMU_PATH}\" -i \"${ENERGYPLUS_PATH}\" -w \"${EPW_PATH}\" -a 2 \"${IDF_PATH}\" 2>/shared/logs/errors.log; \
     echo 'EnergyPlusToFMU execution completed! Logs are available at /shared/logs/errors.log'"]
