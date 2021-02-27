# Team 29 UMD Data Challenge 2021

Common repository for all analysis done on the 2021 UMD data challenge

## Boundary:
- Implemented point in polygon algorithm
- Stored campus, metro, commercial, and geofence boundaries as persistent data using Python's pickle library

## Rides:
- Calculated how many rides originated on campus and terminated off campus and the average distance
- Calculated the same for rides that originated off campus and terminated on campus
- Classified rides by their class using point in polygon algorithm
  - A for in campus -> in campus
  - B for in campus -> out campus
  - C for out campus -> in campus
  - D for out campus -> out campus

## Visualization:
  - Can load up College Park map from GIS provider and draw the polygon bounding box for UMD. 
  - Calculated point density for the number of times a particular location was pinged and visualized it using a heatmap.
