import pandas as pd

tracking = pd.read_csv('with-distance.csv')
ports = pd.read_csv('ports.csv')
df = tracking.merge(ports, left_on=['p_lat','p_long'], right_on=['lat','long'])
df = df.drop(columns=['lat_y','long_y'])
print(df.describe())