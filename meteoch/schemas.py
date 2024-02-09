from pydantic import BaseModel, validator
from meteoch.config import STATION_LIST

class Coldwave(BaseModel):
    station: str

    @validator('station')
    def check_station(cls, station):
        print(f"STATION: {station}")
        if station not in STATION_LIST:
            raise ValueError(f"{station} is not in STATION_LIST")
        return station
