from pandas import DataFrame

from business.dto.exception.custom_exception import CustomException
from business.dto.request.get_address_by_city_request import GetAddressByCityRequest
from business.dto.response.get_address_by_city_response import GetAddressByCityResponse
from business.i_address_service import IAddressService
from persistence.entities.city_entity import CityEntity
from persistence.entities.street_entity import StreetEntity
from persistence.i_city_repository import ICityRepository
from persistence.i_street_repository import IStreetRepository
from persistence.impl.city_repository_impl import CityRepositoryImpl
from persistence.impl.street_repository_impl import StreetRepositoryImpl

import pandas as pd
import os


class AddressServiceImpl(IAddressService):

    # Constructor
    def __init__(self):
        self._city_repository: ICityRepository = CityRepositoryImpl()
        self._streets_repository: IStreetRepository = StreetRepositoryImpl()

    '''
    Service to get addresses by city name
    
    * if city not found, throw an exception with bad request status
    * if more than one city found, throw an exception with bad request status
    * if only one city found, return list of street names

    '''
    def get_address_by_city(self, request: GetAddressByCityRequest) -> GetAddressByCityResponse:

        if self._city_repository.is_empty():
            self.__read_datasets()

        cities: list[CityEntity] = self._city_repository.get_cities_by_name(request.city_name)

        if len(cities) < 1:
            raise CustomException("CITY NOT FOUND!", 400)

        if len(cities) > 1:
            raise CustomException("MORE THAN ONE CITY IS FOUND!", 400)

        streets: list[StreetEntity] = self._streets_repository.get_streets_by_city(cities[0])
        street_names: list[str] = list(street.get_name for street in streets)
        response: GetAddressByCityResponse = GetAddressByCityResponse(street_names=street_names)
        return response

    # Read datasets
    def __read_datasets(self):
        df: DataFrame = pd.read_json("dataset/cities.json", orient="records")
        df['name'] = df["elements"].apply(lambda x: x['tags']['name'])
        df = df.drop(columns=['elements'], axis=1)

        cities: list[CityEntity] = []
        for index, row in df.iterrows():
            cities.append(CityEntity(id=int(str(index)), name=row["name"]))

        self._city_repository.add_cities(cities)

        json_files: list = [file for file in os.listdir("dataset/street")]
        streets: list[StreetEntity] = []

        for json_file in json_files:
            file_path: str = os.path.join("dataset/street", json_file)

            df: DataFrame = pd.read_json(file_path, orient="records")
            df["name"] = df["features"].apply(lambda x: x['properties']['name'] if "name" in x["properties"] else None)
            df = df.drop(columns=['features'], axis=1)

            city: CityEntity = next((c for c in cities if c.get_name == os.path.splitext(json_file)[0]), None)

            for index, row in df.iterrows():
                if row["name"] is not None:
                    streets.append(StreetEntity(id=int(str(index)), name=row['name'], city=city))

            self._streets_repository.add_streets(streets)
