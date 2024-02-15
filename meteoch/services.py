"""Module containing the services used by the API"""
from meteoch.config import STATIONS, MODELS_DET, MODELS_ENS, PARAMETERS, PRODUCTS, INTERFACE
from meteoch.retrieve import retrieve
from meteoch.compute import Threshold_pc
from meteoch.graph import coldwave_graph

def compute_coldwave_graph(station: str):
    # define parameters used for coldwave
    base_url = MODELS_ENS['url']
    lat = STATIONS[station]['lat']
    long = STATIONS[station]['long']
    model = MODELS_ENS['model']['dwd_icon_eps_seamless']['model']
    param = PARAMETERS['t2m']['parameter']
    granularity = PARAMETERS['t2m']['granularity']
    title = PRODUCTS['coldwave']['title'].replace("{station}", STATIONS[station]['name'])
    threshold0 = PRODUCTS['coldwave']['thresholds'][0]
    threshold1 = PRODUCTS['coldwave']['thresholds'][1]
    threshold2 = PRODUCTS['coldwave']['thresholds'][2]

    # generate url used to retrieve data from open-meteo.com
    url = f"{base_url}?latitude={lat}&longitude={long}&{granularity}={param}&models={model}"

    # retrieve data from open-meteo.com
    data = retrieve(url, granularity)

    threshold_pc = Threshold_pc(data)

    thresholds0 = threshold_pc.pc(threshold0, 'min')
    thresholds1 = threshold_pc.pc(threshold1, 'min')
    thresholds2 = threshold_pc.pc(threshold2, 'min')

    x = threshold_pc.abscissa()

    graph = coldwave_graph(x, thresholds0, thresholds1, thresholds2, title)

    return graph
