from abc import ABC, abstractmethod

from persistence.entities.city_entity import CityEntity


class ICityRepository(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def get_cities(self, city_name) -> list[CityEntity]:
        pass

    @abstractmethod
    def add_cities(self, cities: list[CityEntity]) -> None:
        pass

