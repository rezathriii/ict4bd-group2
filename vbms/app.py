from src.helpers import validate_fmu

problems = validate_fmu("../shared/opt_model.fmu")

print(problems)
