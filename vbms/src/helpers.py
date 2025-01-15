import json
from eppy.modeleditor import IDF
from CONSTANTS import *


def list_unique_zones(idf_file_path):
    IDF.setiddname(IDD_FILE_PATH)

    idf = IDF(idf_file_path)

    zones = idf.idfobjects['ZONE']

    unique_zones = {zone.Name for zone in zones}

    return json.dumps(list(unique_zones))


print(list_unique_zones(IDF_FILE_PATH))
