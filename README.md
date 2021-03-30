# rsoft-heatmap-csv
This is a script to convert RSOFT heatmap data to CSV file for plotting using Veusz.

# Usage guide
This script operates as a command line tool with the following command:

```python
/path/to/rsoft-heatmap-csv.py f=mosttmp_dm_de_a_total_vs_wavelength.dat
```
The output file will be generated in the same directory.

# Note for Veusz Users

Use the **Import Data** function:
* Step 1: Select the CSV file converted by this script
* Step 2: Select tab **"2D"**, in section **"X, Y Ranges"**, choose **"Grid points at adges"**