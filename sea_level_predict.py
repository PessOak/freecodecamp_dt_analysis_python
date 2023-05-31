import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df_sea = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
  
    plt.scatter(df_sea["Year"], df_sea["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    x = df_sea["Year"]
    y = df_sea["CSIRO Adjusted Sea Level"]

    x_prev = pd.Series([i for i in range(1880,2051)])
    y_prev = linregress(x,y).slope * x_prev + linregress(x, y).intercept

    plt.plot(x_prev, y_prev, "darkgreen")

    # Create second line of best fit

    df_2000 = df_sea[df_sea["Year"] >= 2000]
    x_2000 = df_2000["Year"]
    y_2000 = df_2000["CSIRO Adjusted Sea Level"]
    

    x_prev2 = pd.Series([i for i in range(2000,2051)])
    y_prev2 = linregress(x_2000, y_2000).slope * x_prev2 + linregress(x_2000, y_2000).intercept
    

    plt.plot(x_prev2, y_prev2, "gray")

    # Add labels and title

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()