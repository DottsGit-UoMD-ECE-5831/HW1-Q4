# Matthew Kwan
# ECE5831 -- Pattern Recognition/Neural Networks
# June 24, 2024
# Homework 1
# Q4b

import numpy as np
import matplotlib.pyplot as plt

# Helpful constants
MILLION = 1000000
HUNDRED_MILLION = 100*MILLION

# fatality_rate of 1.09 per 100M miles
R = .999999989
C = .95

# Should come out to 275 million failure-free miles
n = np.log(1-C) / np.log(R)

print("Number of failure-free miles needed to achieve a reliability rate of {0} with a {1}% confidence level: {2:.4g} million\n".format(R,C*100,n/MILLION))

# Given a fleet of:
# 100 autonomous vehicles,
NUM_VEHICLES = 100
# 24 h a day being test-driven,
HOURS_PER_DAY = 24
# 365 days a year,
DAYS_PER_YEAR = 365
# 25 miles per hour average speed
AVG_MPH = 25

# num of years = num_miles/avg_mph converted to years divided by 100 cars
num_years = n/AVG_MPH * (1/HOURS_PER_DAY) * (1/DAYS_PER_YEAR) / NUM_VEHICLES

# Should come out to about 12.5 years
print("Number of years for {0} cars driven constantly at {1}mph to achieve this reliability rate: {2:.4g} years\n".format(NUM_VEHICLES, AVG_MPH, num_years))

##############
plt.figure(figsize=(10, 6))

C_values = [0.99, 0.95, 0.75, 0.50]
C_colors = ['red', 'green', 'orange', 'blue']
ref_lines = [1.09, 77, 103, 190, 382]

for idx, c in enumerate(C_values):
    # Define a range of R values betw 0 and 1 (exclusive)
    R_values = np.linspace(0.0000000000001, 0.99999999999, 500)
    
    # Calculate corresponding n values
    n_values = np.log(1 - c) / np.log(R_values)
    
    # Plotting 
    plt.plot((1-R_values)*HUNDRED_MILLION, n_values/MILLION, label="C = {0:2g}%".format(c*100), color=C_colors[idx], linewidth=2)

for ref in ref_lines:
    plt.axvline(x=ref, color='black', linestyle='--')
    # 0.89 and 0.11 just shifts the text to align nicely with this chart
    plt.text(ref*0.89, 0.11, "{}".format(ref), rotation=90, va='bottom', color='black')

plt.xlim([0.5, 500])
plt.ylim([0.1, 700])
plt.xscale('log')  # Set logarithmic scale on the x-axis
plt.yscale('log')  # Set logarithmic scale on the y-axis
plt.xlabel('Failure rate (failures per 100 million miles)')
plt.ylabel('Miles needed to be driven (millions)')
plt.title('Failure-free miles needed to demonstrate maximum failure rate')
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()