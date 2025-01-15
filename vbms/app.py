from fmpy import simulate_fmu

# Simulate FMU
result = simulate_fmu('../idfToFMU/optimized.fmu', start_time=0, stop_time=86400, step_size=3600,
                      output=['Zone Mean Air Temperature'])

# Extract Results
for time, temperature in zip(result['time'], result['Zone Mean Air Temperature']):
    print(f"Time: {time}, Temperature: {temperature}")
