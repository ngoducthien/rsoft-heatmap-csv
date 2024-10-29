# RSOFT Heatmap to CSV Converter

This script converts RSOFT heatmap data into CSV format for plotting with Veusz.

# Usage guide

This script operates as a command-line tool. To use it, run the following command:

```bash
/path/to/rsoft-heatmap-csv.py -f=mosttmp_dm_de_a_total_vs_wavelength.dat
```

The output CSV file will be generated in the same directory as the input file.

# Instructions for Veusz Users

1. Open Veusz and navigate to **Import Data**.
2. Select the CSV file generated by this script
3. In the **2D** tab, under the **X, Y Ranges**, choose **Grid points at adges**

