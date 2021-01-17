import pandas as pd
import time
from influxdb import InfluxDBClient

if __name__ == '__main__':
    host = 'localhost'
    port = 8086
    database = 'sample'
    filePath = 'data/sample_data.txt'
    
    client = InfluxDBClient(host=host, port=port, database=database)
    client.create_database(database)

    data= pd.read_csv(filePath, chunksize=60*60*24, header=None, sep=';')

    for batch_data in data:
        rows = batch_data[0].values.tolist()
        client.write(rows, params={'db': database}, protocol='line')
        rows.clear()
        time.sleep(0.1)

    print('finish!')
