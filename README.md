# ATMS-523-Module-4

Module 4 Homework - SeungUk Kim

## Overview
This is a description about the jupyter notebook for Fall 2022 - ATMS 523 Homework4. `Module4.ipynb` is divided into 3 parts, preprocessing data, EOF analysis, and reconstruction.
Monthly ERA5 sea surface temperature, total precipitation, land-sea mask data from ERA5 [cds.climate.copernicus.eu](cds.climate.copernicus.eu) are used.

### Data preparation
`get_lsm.py` and `get_sst_pp.py` are python codes to download lsm, sst, and tp from Copernicus and save to local machine. To avoid errors, complexity of getting 'total' precipitation, and to work with consistent grid setting, NCAR RDA is not used.

### Part 1 & 2 - Preprocessing
SST and TP data are deseasonalized, detrended, and standardized.

### Part 3 & 4 - EOF Analysis
EOF analysis is done and spatial patterns of 5 leading modes, and explained variances of 10 leading modes are explored.

### Part 5 & 6 - Reconstruction
Reconstructed SST pattern is compared with observed SST. And EOF1 is compared with standardized precipitation.
