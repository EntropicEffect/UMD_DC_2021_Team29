#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def discard_outliers_from_path(x,center_lon = -76.9388, center_lat = 38.9896, deg_extent = 0.03):
    results = []
    for coords in x:
        if( (np.abs(coords[0] - center_lon) < deg_extent) and (np.abs(coords[1] - center_lat) < deg_extent)):
            results.append(coords)
    return results

def extract_path_points_from_df(df):
        path_list = df['PATH'][:]
        all_points = []
        points = []
        for str in path_list:
            points.extend(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str))
        path = list(map(float,points))
        zipped = list(zip(points[::2],points[1::2]))
        all_points.extend(discard_outliers_from_path(zipped,center_lon, center_lat, deg_extent))
        return np.array(all_points)

