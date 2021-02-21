# This program counts how many rides start on campus and end outside campus,
# start outside campus and end on campus, etc.

import pandas as pd
import numpy as np
import pickle
from point import Point

df = pd.read_csv('./scooters.csv')
df = df[['DISTANCE', 'START LAT', 'START LONG', 'END LAT', 'END LONG']]
with open('cpk_boundary.pickle', 'rb') as handle:
    umd_bdry = pickle.load(handle)

on_off = []
off_on = []

for index, row in df.iterrows():
  distance, start_lat, start_long, end_lat, end_long = row
  start = Point(start_lat, start_long)
  end = Point(end_lat, end_long)

  start_campus = umd_bdry.point_inside(start)
  end_campus = umd_bdry.point_inside(end)

  # If we start on campus and end outside of campus
  if start_campus == 1 and end_campus == 0:
    on_off.append(row)
  # If we start outside of campus and end inside campus
  elif start_campus == 0 and end_campus == 1:
    off_on.append(row)

on_off = np.array(on_off)
off_on = np.array(off_on)

# 1b
print(f'{len(on_off)} unique rides start on campus and end off campus.')

# 1c
print(f'{len(off_on)} unique rides start off campus and end on campus.')

avg_on_off = sum(on_off[:,0])/len(on_off)
avg_off_on = sum(off_on[:,0])/len(off_on)

# 1b, Part i
print(f'{avg_on_off} was the average distance traveled for on to off campus.')

# 1c, Part i
print(f'{avg_off_on} was the average distance traveled for off to on campus.')

df_on_off = pd.DataFrame(data=on_off, columns=df.columns)
df_off_on = pd.DataFrame(data=off_on, columns=df.columns)

df_on_off.to_csv('on_to_off_campus.csv')
df_off_on.to_csv('off_to_on_campus.csv')