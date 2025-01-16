from fmpy import simulate_fmu
from fmpy import read_model_description, instantiate_fmu

# Read the model description
model_description = read_model_description('./modelDescription.xml')
print(model_description.modelVariables)

# Try instantiating
instance = instantiate_fmu('/root/idf2fmu', model_description)
instance.terminate()
#
# result = simulate_fmu('./opt_model.fmu', start_time=0, stop_time=86400, step_size=3600,
#                       output=['Zone Mean Air Temperature'])
#
# for time, temperature in zip(result['time'], result['Zone Mean Air Temperature']):
#     print(f"Time: {time}, Temperature: {temperature}")
