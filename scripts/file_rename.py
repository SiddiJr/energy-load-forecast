import pandas as pd
import os
import shutil

shutil.copytree('data/raw', 'data/raw_backup')

path = 'data/raw'
columns = ['name', 'latitude', 'longitude', 'altitude']
df = pd.DataFrame(columns=columns)

for filename in os.listdir(path):
    if filename.endswith(".csv") and not filename.startswith('curve'):
        with open(path + '/' + filename, "r") as file:
                station_name = file.readline().replace('Nome: ', '').replace(' - ', '_').replace(' ', '_').lower()
                file.readline()
                station_latitude = file.readline().replace('Latitude: ', '')
                station_longitude = file.readline().replace('Longitude: ', '')
                station_altitude = file.readline().replace('Altitude: ', '')

        row = {
            "name": station_name.replace('\n', ''),
            "latitude": station_latitude.replace('\n', ''),
            "longitude": station_longitude.replace('\n', ''),
            "altitude": station_altitude.replace('\n', '')
        }

        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df = df.map(lambda x: x.replace('\n', ''))
        os.rename(path + '/' + filename.replace('\n', ''), path + '/' + station_name.replace('\n', '') + '.csv')
        df.to_csv('data/clean/stations_metadata.csv')
