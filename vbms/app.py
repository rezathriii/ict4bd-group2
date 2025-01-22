import gym
import numpy as np

env = gym.make('EnergyPlus-v0',
               idf_file="/shared/opt_model.idf",
               weather_file="/shared/weather.epw",
               fmu_file="/shared/opt_model.fmu")

thermal_zones = [
    "Block2CorridorX2fTemperature",
    "Block1OfficeXNWX1fTemperature",
    "Block2OfficeXSWX2fTemperature",
    "Block2OfficeXSEX2fTemperature",
    "Block1OfficeXSWX1fTemperature",
    "Block2OfficeXNWX2fTemperature",
    "Block1OfficeXNEX1fTemperature",
    "Block1CorridorX1fTemperature",
    "Block2OfficeXNEX2fTemperature",
    "Block1OfficeXSEX1fTemperature"
]

obs = env.reset()

# Run the simulation step-by-step
done = False
while not done:
    obs, reward, done, info = env.step([])

    print("Time Step:", info.get("timestep", "Unknown"))
    for zone in thermal_zones:
        if zone in obs:
            print(f"{zone}: {obs[zone]} °C")

    print("-" * 50)

env.close()
