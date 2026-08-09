import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Tyrannosaurus_jaw_closing_accelerations.xlsx - Sheet1.csv", header = None) 
time = data.iloc[1:33, 31]
time = pd.to_numeric(time, errors="coerce") # convert to numbers
valid_time = time.notna()
time = time[valid_time]

for i in range(4):

    alpha = float(data.iloc[2+i, 27]) #angular acceleration

    angular_velocity = alpha * time #angular velocity


    # Plot
    plt.plot(time, angular_velocity)

    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (radians/s)")
    plt.title(f"T. rex Jaw Closing: Angular Velocity vs. Time for angular acceleration\n a = {alpha} rad/ s^2")
    plt.grid(True)

    plt.show()