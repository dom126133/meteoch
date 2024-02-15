from pydantic import BaseModel, validator, Field
import pandas.core.frame
from meteoch.config import STATION_LIST

class Coldwave(BaseModel):
    station: str = "gve"

    @validator('station')
    def check_station(cls, station):
        #print(f"STATION: {station}")
        if station not in STATION_LIST:
            raise ValueError(f"{station} is not in STATION_LIST")
        return station

class Mosmix_tntx(BaseModel):
    synopid: str = Field(default="06700", description="Valid synop ID in Europa")
