import json
from eppy.modeleditor import IDF
from src.CONSTANTS import *
from fmpy.validation import validate_fmu


def list_unique_zones(idf_file_path):
    IDF.setiddname(IDD_FILE_PATH)

    idf = IDF(idf_file_path)

    zones = idf.idfobjects['ZONE']

    unique_zones = {zone.Name for zone in zones}

    return json.dumps(list(unique_zones))


def fmu_validation(fmu_path="/shared/opt_model.fmu"):
    validation_result = validate_fmu(fmu_path)

    print("\n🔍 FMU Validation Result:")
    print(validation_result)


# print(list_unique_zones("../../shared/opt_model.idf"))
