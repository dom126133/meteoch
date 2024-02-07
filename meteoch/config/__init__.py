import os

# if python version < 3.11, use tomli insatead of tomllib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


# parse config files
with open('/'.join([os.path.realpath(os.path.dirname(__file__)),"stations.toml"]), mode='rb') as fp:
    STATIONS = tomllib.load(fp)

with open('/'.join([os.path.realpath(os.path.dirname(__file__)),"models_det.toml"]), mode='rb') as fp:
    MODELS_DET = tomllib.load(fp)

with open('/'.join([os.path.realpath(os.path.dirname(__file__)),"models_ens.toml"]), mode='rb') as fp:
    MODELS_ENS = tomllib.load(fp)
    
with open('/'.join([os.path.realpath(os.path.dirname(__file__)),"parameters.toml"]), mode='rb') as fp:
    PARAMETERS = tomllib.load(fp)


