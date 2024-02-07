from config import STATIONS, MODELS_DET, MODELS_ENS, PARAMETERS
import retrieve
import calculs

url = MODELS_ENS['url']
print(f"URL: {url}")
station = 'gve'
lat = STATIONS[station]['lat']
long = STATIONS[station]['long']
model = MODELS_ENS['model']['dwd_icon_eps_seamless']['model']
param = PARAMETERS['t2m']['param']
type = PARAMETERS['t2m']['kind']

full_url = f"{url}?latitude={lat}&longitude={long}&{type}={param}&models={model}"
print(full_url)

data = retrieve.retrieve(full_url, type)

#print(data)

threshold_pc = calculs.Threshold_pc(data)

thresholds = threshold_pc.pc(0)

print("Date         % < 0 °C")
for threshold in thresholds:
    print(f"{threshold[0]:<12}   {threshold[2]:<5}")