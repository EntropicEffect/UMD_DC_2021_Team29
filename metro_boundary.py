from point import Point
from polygon import Polygon
import os
import pickle

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'metro_boundary')
points = []
with open(filename) as file:
    for line in file.readlines():
        p = line.split(', ')
        points.append(Point(float(p[0]), float(p[1])))

poly = Polygon(points)

with open('boundaries/metro/metro_boundary.pickle', 'wb') as handle:
    pickle.dump(poly, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('boundaries/metro/metro_boundary.pickle', 'rb') as handle:
    metro_boundary = pickle.load(handle)
    
print(metro_boundary)