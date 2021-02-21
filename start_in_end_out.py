import pandas as pd
import pickle
from point import Point

df = pd.read_csv('./scooters.csv')
df = df[['START LAT', 'START LONG', 'END LAT', 'END LONG']]

print(df.head(10))

with open('cpk_boundary.pickle', 'rb') as handle:
    umd_bdry = pickle.load(handle)

count = 0
for index, [start_lat, start_long, end_lat, end_long] in df.iterrows():
  start = Point(start_lat, start_long)
  end = Point(end_lat, end_long)

  start_in_campus = umd_bdry.point_inside(start) == 1
  end_off_campus = umd_bdry.point_inside(end) == 0
  if start_in_campus and end_off_campus:
    count += 1

print(count) # 7233 unique rides start in campus and end off campus