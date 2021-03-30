#!/usr/bin/env python3.7.9
# -*- Coding: UTF-8 -*-

import numpy as np
from netCDF4 import Dataset
import sys
lat_p = np.float(sys.argv[1])
lon_p = np.float(sys.argv[2])

filename = 'example.nc'
dataset = Dataset(filename)
varname = 'CPD'
time = -1

def latlon_finder(dataset, lat_p, lon_p):
    '''
    Find pixel center closest to given lat/lon
    '''
    lat = dataset.variables['latitude'][:]
    lon = dataset.variables['longitude'][:]
    lat_i = (np.abs(lat-lat_p)).argmin()
    lon_j = (np.abs(lon-lon_p)).argmin()
    return lat_i, lon_j

def get_pixel_value(dataset, lat_i, lon_j, varname, time):
    '''
    Get value from lat_p and lon_p pixel
    1: multiple times
    -1: one time
    '''
    var = dataset.variables[varname][:]
    if time >= 0:
        result = var[time][lat_i][lon_j]
    else:
        result = var[lat_i][lon_j]
    return result

lat_i, lon_j = latlon_finder(dataset, lat_p, lon_p)
value = get_pixel_value(dataset, lat_i, lon_j, varname, time)

print(value)
