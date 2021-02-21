# This program counts how many rides start on campus and end outside campus,
# start outside campus and end on campus, etc.

# This program aims to answer questions 1(b) and 1(c). (At least the first part
# in those multipart questions.)

import pandas as pd
import pickle
from point import Point

df = pd.read_csv('./scooters.csv')
df = df[['START LAT', 'START LONG', 'END LAT', 'END LONG']]

with open('cpk_boundary.pickle', 'rb') as handle:
    umd_bdry = pickle.load(handle)

on_off_count = 0
off_on_count = 0
off_off_count = 0
on_on_count = 0

for index, [start_lat, start_long, end_lat, end_long] in df.iterrows():
  start = Point(start_lat, start_long)
  end = Point(end_lat, end_long)

  start_campus = umd_bdry.point_inside(start)
  end_campus = umd_bdry.point_inside(end)

  # If we start on campus and end outside of campus
  if start_campus == 1 and end_campus == 0:
    on_off_count += 1
  # If we start outside of campus and end inside campus
  elif start_campus == 0 and end_campus == 1:
    off_on_count += 1
  # If we start outside of campus and end outside campus
  elif start_campus == 0 and end_campus == 0:
    off_off_count += 1
  # If we start inside campus and end inside campus
  else:
    on_on_count += 1

print(f'{on_off_count} unique rides start on campus and end off campus.')
print(f'{off_on_count} unique rides start off campus and end on campus.')
print(f'{on_on_count} unique rides start on campus and end on campus.')
print(f'{off_off_count} unique rides start off campus and end off campus.')