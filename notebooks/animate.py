# Convert 'Time' from timedelta to total seconds for plotting
# Import required modules
import io
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import datetime
import streamlit as st
from matplotlib.animation import FuncAnimation

# set the directories
base_path = os.path.dirname(os.path.realpath("__file__"))
root_path = os.path.join(base_path, "..")
data_path = os.path.join(root_path, "data")
images_path = os.path.join(root_path, "images")

# Read the data
marathon_data_df = pd.read_csv(os.path.join(data_path, "marathon_data_cleaned.csv"))

# Convert time seconds to datetime
marathon_data_df["Time"] = pd.to_datetime(marathon_data_df["Time"]).dt.time

plt.style.use("../styles/plotstyle.mplstyle")  # Use custom style
marathon_data_df["Time_seconds"] = marathon_data_df["Time"].dt.total_seconds()

# Convert time seconds to datetime
marathon_data_df["Time_seconds"] = pd.to_datetime(
    marathon_data_df["Time_seconds"], unit="s"
).dt.time

# Assuming 'data' is a DataFrame with 'Year' and 'Time_seconds' columns for Kenyan athletes
data_sorted = marathon_data_df.sort_values(by="Time_seconds")


def animate():
    fig, ax = plt.subplots()
    (line,) = ax.plot([], [], "r-")  # Starting with an empty line
    ax.set_xlim(data_sorted["Year"].min(), data_sorted["Year"].max())
    ax.set_ylim(data_sorted["Time_seconds"].min(), data_sorted["Time_seconds"].max())

    def init():
        line.set_data([], [])
        return (line,)

    def update(frame):
        x = data_sorted["Year"].iloc[:frame]
        y = data_sorted["Time_seconds"].iloc[:frame]
        line.set_data(x, y)
        return (line,)

    ani = FuncAnimation(
        fig, update, frames=range(len(data_sorted)), init_func=init, blit=True
    )
    return ani


if __name__ == "__main__":
    ani = animate()
    plt.show()
    ani.save(
        os.path.join(images_path, "marathon_animation.gif"),
        writer="imagemagick",
        fps=10,
    )
