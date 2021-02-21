# This program counts how many rides start on campus and end outside campus,
# start outside campus and end on campus, etc.

import pandas as pd
import pickle
from point import Point

df = pd.read_csv('./scooters.csv')
df = df[['DISTANCE', 'START LAT', 'START LONG', 'END LAT', 'END LONG']]

with open('cpk_boundary.pickle', 'rb') as handle:
    umd_bdry = pickle.load(handle)

on_off_count = 0
off_on_count = 0
off_off_count = 0
on_on_count = 0

on_off_distance = 0
off_on_distance = 0
off_off_distance = 0
on_on_distance = 0

for index, [distance, start_lat, start_long, end_lat, end_long] in df.iterrows():
  start = Point(start_lat, start_long)
  end = Point(end_lat, end_long)

  start_campus = umd_bdry.point_inside(start)
  end_campus = umd_bdry.point_inside(end)

  # If we start on campus and end outside of campus
  if start_campus == 1 and end_campus == 0:
    on_off_distance += distance
    on_off_count += 1
  # If we start outside of campus and end inside campus
  elif start_campus == 0 and end_campus == 1:
    off_on_distance += distance
    off_on_count += 1
  # If we start outside of campus and end outside campus
  elif start_campus == 0 and end_campus == 0:
    off_off_count += 1
    off_off_distance += distance
  # If we start inside campus and end inside campus
  else:
    on_on_count += 1
    on_on_distance += distance

# 1b
print(f'{on_off_count} unique rides start on campus and end off campus.')

# 1c
print(f'{off_on_count} unique rides start off campus and end on campus.')

avg_on_off = on_off_distance/on_off_count
avg_off_on = off_on_distance/off_on_count

# 1b, Part i
print(f'{avg_on_off} was the average distance traveled for on to off campus.')

# 1c, Part i
print(f'{avg_off_on} was the average distance traveled for off to on campus.')