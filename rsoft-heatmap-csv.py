"""
This is a script to convert RSOFT heatmap to CSV format for plotting
using Veusz.
"""


import pandas as pd
import numpy as np
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument(
    '-f', '-file', '--filename',
    help="Rsoft heatmap filename",
    dest='filename',
    type=str,
    nargs='*',
    required=True
)

args = parser.parse_args()
filename = args.filename[0]

# Extracting extension from filename
file, file_extension = os.path.splitext(filename)

# Read heatmap data from RSOFT output
data = pd.read_csv(
    filename,
    sep=r'\s+',
    skiprows=4,
    header=None
)

# Tranpose the data
data = data.T

# Read header and index from RSOFT output
with open(filename) as target:
    head = [next(target) for x in range(4)]

x_axis = head[2].strip().split(' ')
y_axis = head[3].strip().split(' ')

x_array = np.linspace(float(x_axis[1]), float(x_axis[2]), int(x_axis[0]))
y_array = np.linspace(float(y_axis[1]), float(y_axis[2]), int(y_axis[0]))

data.columns = x_array
data.index = y_array

# Save data to CSV file
data.to_csv('{0}.CSV'.format(file), float_format='%.8E')
