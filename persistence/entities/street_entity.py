from dataclasses import dataclass

from persistence.entities.city_entity import CityEntity


@dataclass
class StreetEntity:

    # Constructor for StreetEntity
    def __init__(self, city: CityEntity, id: int, name: str):
        self._id: int = id
        self._name: str = name
        self._city: CityEntity = city

    # Getter for city
    @property
    def get_city(self) -> CityEntity:
        return self._city

    # Getter for street name
    @property
    def get_name(self) -> str:
        return self._name
