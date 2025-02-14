import pandas as pd

if __name__ == "__main__":
    print('hello')

    readings = pd.read_csv('readings.csv')
    print(readings)

    stations = pd.read_csv('stations.csv')
    print(stations)

    sensors = pd.read_csv('sensors.csv')
    stations_sensors = pd.read_csv('stations_sensors.csv')
    print(sensors)
    print(stations_sensors)

    print(readings.columns)
    print(stations.columns)

    join_inner = readings.join(stations.set_index('id'), how='inner')
    print(join_inner)

    sens_joined = sensors.join(stations_sensors.set_index('sensor_id'), how='outer', on='id')
    print(sens_joined)

    '''
    df1 = pd.DataFrame({'key': ['a','b','c','d','e','f'], "data1": [1,2,3,7,8,9]})
    df2 = pd.DataFrame({'key': ['a','b','c'], "data2": [4,5,6]})

    df3 = df1.join(df2.set_index('key'), how='inner', on='key')
    print(df3)

    joined_outer = df1.set_index('key').join(df2.set_index('key'),how="outer")
    print(joined_outer)
    '''