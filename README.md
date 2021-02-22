Common repository for all analysis done on the 2021 UMD data challenge

#Boundary:
- Implemented point in polygon algorithm
- Stored boundary as persistent data using pickle (don't have to rescrape data to get boundary)

#Rides:
- Calculated how many rides originated on campus and terminated off campus and the average distance
- Calculated the same rides that originated off campus and terminated on campus

#Trips:
- Classified trips by their class (A for in campus -> in campus, B for in campus -> out campus, C for out campus -> in campus)

#Visualization:
  - Can load up College Park map from GIS provider and draw the polygon bounding box for UMD. 
  - Calculated heatmap intensity for the number of times a particular location was pinged. Cannot yet overlay this on GIS provided map
