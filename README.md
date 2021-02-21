Common repository for all analysis done on the 2021 UMD data challenge

Boundary:
- Implemented point in polygon algorithm
- Stored boundary as persistent data using pickle (don't have to rescrape data to get boundary)

Rides:
- Calculated how many rides originated on campus and terminated off campus and the average distance
- Calculated the same rides that originated off campus and terminated on campus
- The data for each is stored in its respective csv file. 
  - *Note:* data only contains 'DISTANCE', 'START LAT', 'START LONG', 'END LAT', 'END LONG' right now, can update this later if needed!

Visualization:
  - Can load up College Park map from GIS provider and draw the polygon bounding box for UMD. 
  - Calculated heatmap intensity for the number of times a particular location was pinged. Cannot yet overlay this on GIS provided map
