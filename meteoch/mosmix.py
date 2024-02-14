# Copyright (C) 2018-2021, earthobservations developers.
# Distributed under the MIT License. See LICENSE for more info.
"""
=====
About
=====
Example for DWD MOSMIX acquisition.

This program will request latest MOSMIX-L data for
stations_result 06700 and parameters DD and ww.

Other MOSMIX variants are also listed and can be
enabled on demand.
"""  # Noqa:D205,D400
from wetterdienst import Settings
from wetterdienst.provider.dwd.mosmix import (
    DwdForecastDate,
    DwdMosmixRequest,
    DwdMosmixType,
)
from wetterdienst.util.cli import setup_logging

import pandas as pd
import pandas.core.frame

def mosmix_tntx(synopid:str="06700")->list[pandas.core.frame.DataFrame, pandas.core.frame.DataFrame]:
    """Retrieve Mosmix mosmix data by DWD."""
    # A. MOSMIX-L -- Specific stations_result - each station with own file
    settings = Settings(ts_shape=True, ts_humanize=True)

    request = DwdMosmixRequest(
        parameter=["TN", "TX"],
        start_issue=DwdForecastDate.LATEST,  # automatically set if left empty
        mosmix_type=DwdMosmixType.LARGE,
        settings=settings,
    )

    stations = request.filter_by_station_id(
        station_id=[synopid],
    )

    response = next(stations.values.query())

    # meta data enriched with information from metadata_for_forecasts()
    #_output_section("Metadata", response.stations.df)
    #_output_section("Forecasts", response.df)
    
    # transform polars dataframe to pandas dataframe
    tntx = response.df.to_pandas()

    # drop unnecessary columns
    tntx.drop(columns=['station_id', 'parameter', 'dataset', 'quality'], inplace=True)

    # convert temperature to Celsius
    tntx['Celsius'] = tntx['value'] - 273.15

    # create tn and tx dataframe
    tn = (tntx.where(tntx['date'].dt.hour == 6))
    tx = tntx.where(tntx['date'].dt.hour == 18)

    # drop NaN row from dataframe
    tn.dropna(inplace=True)
    tx.dropna(inplace=True)

    return [tn, tx]

def _output_section(title, data):  # pragma: no cover
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    print(data)
    print()


def main():
    """Run example."""
    setup_logging()
    [tn, tx] = mosmix_tntx("06700")
    print(f"Tn\n{tn.head(20)}")
    print(f"Tx\n{tx.head(20)}")

if __name__ == "__main__":
    main()
    