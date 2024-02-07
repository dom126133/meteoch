import requests
import pandas as pd

def retrieve(url, kind):
    resp = requests.get(url)
    data =resp.json()

    data_as_list = pd.json_normalize(data[kind])

    data_headers = []
    for item in data_as_list.items():
        data_headers.append(item[0])

    data_hourly = data_as_list.explode(data_headers)
    # convert time (string) in time (datetime)
    data_hourly['time'] = data_hourly['time'].astype('datetime64[ns]')

    return data_hourly
