import os

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
          }

# parse config files
for key in config.keys():
    #print(f"Parsing {config[key]}")
    with open('/'.join([os.path.realpath(os.path.dirname(__file__)),config[key]]), mode='rb') as fp:
        globals()[key] = tomllib.load(fp)

# generate list of stations
STATION_LIST = []
for station in STATIONS:  # type: ignore  # noqa: F821
    STATION_LIST.append(station)
