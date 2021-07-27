import pandas as pd
from scipy.spatial.distance import cdist
from geopy.distance import geodesic

def closest_point(point, points):
    return points[cdist([point], points).argmin()]

tracking  = pd.read_csv('tracking.csv')
ports = pd.read_csv('ports.csv')

print(tracking.tail())
print(ports.tail())

points = list(ports[['lat','long']].to_records(index=False))
points2 = ports[['lat','long']].to_numpy().reshape(-1,2)
print(points2)
#print(points)
'''
for index, row in tracking.iterrows():
    point = (row.lat, row.long)
    print(point)
    closest = closest_point( point, points2)
    print(closest)
    distance = geodesic(point, closest).mi
    row['distance']=distance
'''

def return_distance(latitude, longitude, points):
    point = (latitude,longitude)
    closest = closest_point(point, points)
    out = geodesic(point, closest).mi
    return out, closest

tracking[['distance','closest']] = tracking.apply(lambda x: return_distance(x['lat'], x['long'], points2), axis=1, result_type='expand')
tracking[['p_lat','p_long']]=tracking['closest'].tolist()
tracking = tracking.drop(columns=['closest'])
print(tracking)

tracking.to_csv('with-distance.csv', index=False)