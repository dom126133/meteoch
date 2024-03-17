import os
import pandas as pd

# if python version < 3.11, use tomli instead of tomllib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# list of config files as value and variable name as key
config = {'STATIONS' : 'stations.toml',
          'MODELS_DET' : 'models_det.toml',
          'MODELS_ENS' : 'models_ens.toml',
          'PARAMETERS' : 'parameters.toml',
          'PRODUCTS' : 'products.toml',
          'INTERFACE': 'interface.toml',
          'OPENDATA_DWD': 'opendata_dwd.toml',
          'MOSMIX' : 'mosmix.toml',
          'DIFFDRUCK' : 'diffdruck.toml',
          }
# mosmix cfg file
MOSMIX_CFG = 'mosmix_stations-2024-02-26.csv'

# parse config files
for key in config.keys():
    print(f"Parsing {config[key]}")
    with open('/'.join([os.path.realpath(os.path.dirname(__file__)),config[key]]), mode='rb') as fp:
        globals()[key] = tomllib.load(fp)

# generate list of stations
STATION_LIST = []
for station in STATIONS:  # type: ignore  # noqa: F821
    STATION_LIST.append(station)

# generate mosmix_station_list
CH_MOSMIX_STATIONS = []
for station in MOSMIX['ch']:  # type: ignore  # noqa: F821
    CH_MOSMIX_STATIONS.append(station)

class Mosmix:
    def __init__(self):
        """initialize MosMix class"""

        # construct a pandas pickle to save mosmix data from cfg file
        try:
            mosmix_filename = '/'.join([os.path.realpath(os.path.dirname(__file__)), MOSMIX_CFG])
            self.mosmix = pd.read_csv(mosmix_filename, sep=';')
            self.mosmix.columns = ['ID','ICAO', 'NAME','LAT','LON','ELEV']
        except:
            print(f"unable to read mosmix cfg file: {mosmix_filename}!")

    def mosmix_df(self, land:str='ch')->pd.DataFrame:
        "return a pandas dataframe with Swiss station (06xxx)"
        if land == 'ch':
            mosmix = self.mosmix[self.mosmix['ID'].str.contains(r'^06[6|7|9]\d\d$')]
        else:
            print("error, only ch is available at the moment")
            mosmix = pd.DataFrame() # create empty DataFrame
        return(mosmix)

    def __str__(self) -> str:
        return(self.mosmix.to_string())