from config import STATIONS, MODELS_DET, MODELS_ENS, PARAMETERS
import retrieve
import compute
import itertools

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

threshold_pc = compute.Threshold_pc(data)

thresholds0 = threshold_pc.pc(-5, 'min')
thresholds1 = threshold_pc.pc(0, 'min')
thresholds2 = threshold_pc.pc(5, 'min')

print("Date         % < -5 °C    % < 0 °C    % < 5 °C")
for (threshold0,threshold1,threshold2) in itertools.zip_longest(thresholds0, thresholds1, thresholds2):
    print(f"{threshold0[0]:<12}   {threshold0[2]:<10}   {threshold1[2]:<10}    {threshold2[2]:<5}")