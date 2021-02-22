import matplotlib.pyplot as plt
import pandas as pd
import pickle
import numpy as np
from point import Point

def get_cpk_boundary():
    with open('cpk_boundary.pickle', 'rb') as handle:
        return pickle.load(handle)

def get_trip_class(boundary, row):
    # point inside: 0, 1, 2
        # 0: outside polygon
        # 1: inside polygon
        # 2: on the polygon

    start = Point(row['START LAT'], row['START LONG'])
    end = Point(row['END LAT'], row['END LONG'])
    start_campus = boundary.point_inside(start)
    end_campus = boundary.point_inside(end)

    # Trip classes:
        # A = start and end on campus
        # B = start on campus, end off campus
        # C = start off campus, end on campus

    if start_campus >= 1 and end_campus >= 1:
        return 'A'
    elif start_campus >= 1 and end_campus == 0:
        return 'B'
    elif start_campus == 0 and end_campus >= 1:
        return 'C'
    else:
        return np.NAN

df = pd.read_csv('scooters.csv')
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'PATH', 'TIMESTAMPS'], axis=1)

boundary = get_cpk_boundary()
df['TRIP_CLASS'] = df.apply (lambda row: get_trip_class(boundary, row), axis=1)
df.dropna(subset=['TRIP_CLASS'], inplace=True)

# df.to_csv('RidesWithTripClass.csv')

df1 = df[df['TRIP_CLASS'] == 'A']
df2 = df[df['TRIP_CLASS'] == 'B']
df3 = df[df['TRIP_CLASS'] == 'C']

df12019 = df1[df1['CREATED'].str.startswith('2019')]
df12020 = df1[df1['CREATED'].str.startswith('2020')]
df22019 = df2[df2['CREATED'].str.startswith('2019')]
df22020 = df2[df2['CREATED'].str.startswith('2020')]
df32019 = df3[df3['CREATED'].str.startswith('2019')]
df32020 = df3[df3['CREATED'].str.startswith('2020')]

df2019 = df[df['CREATED'].str.startswith('2019')]
df2020 = df[df['CREATED'].str.startswith('2020')]

## Creates csv files from dataframes

# df12019.to_csv('RidesWithTripClassA2019.csv')
# df12020.to_csv('RidesWithTripClassA2020.csv')
# df22019.to_csv('RidesWithTripClassB2019.csv')
# df22020.to_csv('RidesWithTripClassB2020.csv')
# df32019.to_csv('RidesWithTripClassC2019.csv')
# df32020.to_csv('RidesWithTripClassC2020.csv')