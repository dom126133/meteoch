import requests
import pandas as pd

def retrieve(url, kind):
    """kind is working at least for hourly granularity"""
    resp = requests.get(url)
    data =resp.json()
    #print(data)

    data_as_list = pd.json_normalize(data[kind])

    data_headers = []
    for item in data_as_list.items():
        data_headers.append(item[0])

    data_kind = data_as_list.explode(data_headers)
    # convert time (string) in time (datetime)
    data_kind['time'] = data_kind['time'].astype('datetime64[ns]')

    return data_kind
