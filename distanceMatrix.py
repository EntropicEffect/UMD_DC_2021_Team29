import os

import numpy as np
import pandas as pd
import googlemaps

from tqdm import tqdm


key='AIzaSyC5sm2NcFBwl5_wpwvH8cg-R6AtzHyKAU0'
client = googlemaps.Client(key)

dataFolder = 'C:\\Users\\kevin\\Desktop'
dataFile = 'travelTimes.csv'

df = pd.read_csv(os.path.join(dataFolder, dataFile))

for i in tqdm(range(len(df))):
    origins = [[df['START LAT'][i], df['START LONG'][i]]]
    destinations = [[df['END LAT'][i], df['END LONG'][i]]]

    matrix = client.distance_matrix(
        origins=origins, 
        destinations=destinations,
        mode='walking',
        units='metric')

    travelTimeMinutes = matrix['rows'][0]['elements'][0]['duration']['value'] / 60.0

    #print(travelTimeMinutes)

    df['minutes'][i] = travelTimeMinutes

newDF = df[['START LAT', 'START LONG', 'END LAT', 'END LONG', 'minutes']]

newDF.to_csv(os.path.join(dataFolder, 'travelTimes2.csv'))
