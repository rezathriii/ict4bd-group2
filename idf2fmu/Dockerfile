FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY install_dependencies.sh /app/install_dependencies.sh

RUN chmod +x /app/install_dependencies.sh && /app/install_dependencies.sh

ENV ENERGYPLUSTOFMU_PATH="/app/EnergyPlusToFMU/Scripts/EnergyPlusToFMU.py"
ENV ENERGYPLUS_PATH="/usr/local/EnergyPlus-9-6-0/Energy+.idd"
ENV EPW_PATH="/shared/paris_2005.epw"
ENV IDF_PATH="/shared/opt_model.idf"

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]