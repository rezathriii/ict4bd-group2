#!/bin/bash

mkdir -p /shared/logs
echo 'EnergyPlusToFMU has started...'

cd /shared || exit 1

python3 "${ENERGYPLUSTOFMU_PATH}" -i "${ENERGYPLUS_PATH}" -w "${EPW_PATH}" -L -a 2 "${IDF_PATH}" 2> >(tee /shared/logs/errors_tmp.log >&2)

# Check if there were any errors, if not, remove the temporary log
if [ -s /shared/logs/errors_tmp.log ]; then
    mv /shared/logs/errors_tmp.log /shared/logs/errors.log
else
    rm -f /shared/logs/errors_tmp.log
fi

echo 'EnergyPlusToFMU execution completed!'