from fastapi import FastAPI, Response, status
from pydantic import ValidationError
import uvicorn
import itertools
from meteoch.config import STATIONS, MODELS_DET, MODELS_ENS, PARAMETERS, PRODUCTS, INTERFACE
from meteoch.retrieve import retrieve
from meteoch.compute import Threshold_pc
from meteoch.schemas import Coldwave
from meteoch.graph import coldwave_graph

app = FastAPI(title=INTERFACE['title'])


@app.get("/", status_code = 200)
async def root() -> dict:
    """Root Get"""
    return {"msg": f"{INTERFACE['bienvenue']}"}

@app.get(
    "/coldwave", 
    # Set what the media type will be in the autogenerated OpenAPI specification.
    # fastapi.tiangolo.com/advanced/additional-responses/#additional-media-types-for-the-main-response
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },

    # Prevent FastAPI from adding "application/json" as an additional
    # response media type in the autogenerated OpenAPI specification.
    # https://github.com/tiangolo/fastapi/issues/3258
    response_class=Response,
    status_code=status.HTTP_200_OK
)
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


    x = threshold_pc.abscissa()
    #print(x)
    #print(thresholds0)
    #print(thresholds1)
    #print(thresholds2)

    graph = coldwave_graph(x, thresholds0, thresholds1, thresholds2)

    return Response(content=graph, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("asgi:app", host="127.0.0.1", port=8001, reload=True, log_level='debug')
