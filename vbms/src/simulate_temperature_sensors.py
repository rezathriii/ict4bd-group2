import logging

logging.basicConfig(level=logging.INFO, filename='sensor_simulation.log')


def on_begin_timestep_before_predictor(state):
    """
    This function is called at the beginning of each timestep.
    """
    logging.info("Starting timestep simulation.")

    # Example: Set temperatures for 10 zones
    for zone_num in range(1, 11):
        # Generate a random temperature between 20 and 25 degrees Celsius
        temperature = state.uniform_random_number() * 5 + 20  # EnergyPlus API to generate random numbers
        # Retrieve the handle for the temperature sensor in the zone
        handle = state.get_variable_handle(f"Zone {zone_num} Air Temperature")
        # Set the new temperature value
        state.set_variable_value(handle, temperature)

    logging.info("Timestep simulation completed.")

    return 0
