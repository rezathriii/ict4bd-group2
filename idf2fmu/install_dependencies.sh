#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Updating and installing dependencies..."

apt update && apt upgrade -y
apt install -y unzip g++ libgomp1 libxml2 libxml2-dev \
    build-essential cmake pkg-config wget sudo \
    libx11-6 libxrender1 libxtst6 software-properties-common \
    software-properties-common

apt clean && rm -rf /var/lib/apt/lists/*

echo "Installing Python 3.8..."

add-apt-repository ppa:deadsnakes/ppa
apt update
apt install -y python3.8 python3.8-distutils
apt clean && rm -rf /var/lib/apt/lists/*

echo "Installing EnergyPlus..."

wget "https://github.com/NREL/EnergyPlus/releases/download/v9.6.0/EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu18.04-x86_64.sh"
chmod +x EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu18.04-x86_64.sh
echo "y" | bash EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu18.04-x86_64.sh --silent --prefix=/usr/local/EnergyPlus-9-6-0
rm EnergyPlus-9.6.0-f420c06a69-Linux-Ubuntu18.04-x86_64.sh

echo "Setting up EnergyPlus environment variables..."

echo 'export PATH="/usr/local/EnergyPlus-9-6-0:$PATH"' >> /etc/environment
echo 'export PATH="/usr/local/EnergyPlus-9-6-0:$PATH"' > /etc/profile.d/energyplus.sh
ln -s /usr/local/EnergyPlus-9-6-0/energyplus /usr/bin/energyplus

echo "Installing EnergyPlusToFMU..."

wget "https://github.com/lbl-srg/EnergyplusToFMU/releases/download/v3.1.0/EnergyPlusToFMU-v3.1.0.zip"
mkdir -p /app/EnergyPlusToFMU
unzip EnergyPlusToFMU-v3.1.0.zip -d /app/EnergyPlusToFMU
rm -f EnergyPlusToFMU-v3.1.0.zip

echo "Installation completed successfully!"