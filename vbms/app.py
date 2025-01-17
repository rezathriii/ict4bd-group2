from fmpy import read_model_description
from src.helpers import fmu_validation

fmu_path = "/shared/fmu/opt_model.fmu"
model_description = read_model_description(fmu_path)

fmu_validation(fmu_path)
