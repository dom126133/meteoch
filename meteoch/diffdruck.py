
import pandas as pd
from meteoch.config import PARAMETERS, MODELS_ENS, DIFFDRUCK, STATIONS
from meteoch.retrieve import retrieve

def diffdruck(station1, station2):
    """retrieve QNH pressure from station 1 and 2, does a difference and print ot as a graphic"""

    model = MODELS_ENS['model'][DIFFDRUCK['model']]['model']
    forecast_days = DIFFDRUCK['forecast_days']
    past_days = DIFFDRUCK['past_days']
    granularity = DIFFDRUCK['granularity']
    parameter = DIFFDRUCK['parameter']
    lat1 = STATIONS[station1]['lat']
    long1 = STATIONS[station1]['long']
    lat2 = STATIONS[station2]['lat']
    long2 = STATIONS[station2]['long']
    base_url = MODELS_ENS['url']
    url1 = f"{base_url}?latitude={lat1}&longitude={long1}&{granularity}={parameter}&past_days={past_days}&forecast_days={forecast_days}&models={model}"
    url2 = f"{base_url}?latitude={lat2}&longitude={long2}&{granularity}={parameter}&past_days={past_days}&forecast_days={forecast_days}&models={model}"
    print(url1)
    print(url2)

    # retrieve data from open-meteo.com
    data1 = retrieve(url1, granularity)
    data2 = retrieve(url2, granularity)

    # set index to the 'time' column
    data1.set_index('time', inplace=True)
    data2.set_index('time', inplace=True)

    # compute difference of pressure from station1 minus pressure of station2
    diff = data1 - data2
    # extract  column name from the dataframe as model_no
    model_no = diff.columns

    # compute quantile
    q10 = pd.DataFrame({'Q10':diff.quantile(0.10, axis=1)})
    q25 = pd.DataFrame({'Q25':diff.quantile(0.25, axis=1)})
    q50 = pd.DataFrame({'Q50':diff.quantile(0.50, axis=1)})
    q75 = pd.DataFrame({'Q75':diff.quantile(0.75, axis=1)})
    q90 = pd.DataFrame({'Q90':diff.quantile(0.90, axis=1)})
    quantiles = pd.concat([q10,q25,q50,q75,q90], axis=1, join='inner')
