from fastapi import FastAPI, Response, status
from pydantic import ValidationError
import uvicorn
import itertools
from meteoch.config import STATIONS, MODELS_DET, MODELS_ENS, PARAMETERS, PRODUCTS, INTERFACE
from meteoch.retrieve import retrieve
from meteoch.compute import Threshold_pc
from meteoch.schemas import Coldwave

app = FastAPI(title=INTERFACE['title'])


@app.get("/", status_code = 200)
async def root() -> dict:
    """Root Get"""
    return {"msg": f"{INTERFACE['bienvenue']}"}

@app.get("/coldwave", status_code=status.HTTP_200_OK)
async def coldwave(station:str, response: Response):
    """ColdWave for specified station"""

    try:
        Coldwave(station=station)
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"Error: {str(e)}!"

    Coldwave(station=station)


    # define parameters used coldwave
    base_url = MODELS_ENS['url']
    lat = STATIONS[station]['lat']
    long = STATIONS[station]['long']
    model = MODELS_ENS['model']['dwd_icon_eps_seamless']['model']
    param = PARAMETERS['t2m']['parameter']
    granularity = PARAMETERS['t2m']['granularity']

    # generate url used to retrieve data from open-meteo.com
    url = f"{base_url}?latitude={lat}&longitude={long}&{granularity}={param}&models={model}"

    # retrieve data from open-meteo.com
    data = retrieve(url, granularity)

    threshold_pc = Threshold_pc(data)

    thresholds0 = threshold_pc.pc(-5, 'min')
    thresholds1 = threshold_pc.pc(0, 'min')
    thresholds2 = threshold_pc.pc(5, 'min')

    result_str = ""
    result_str+="Date         % < -5 °C    % < 0 °C    % < 5 °C\n"
    for (threshold0,threshold1,threshold2) in itertools.zip_longest(thresholds0, thresholds1, thresholds2):
        result_str+=f"{threshold0[0]:<12}   {threshold0[2]:<10}   {threshold1[2]:<10}    {threshold2[2]:<5}\n"

    return result_str

if __name__ == "__main__":
    uvicorn.run("asgi:app", host="127.0.0.1", port=8001, reload=True, log_level='debug')


"""
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

"""
