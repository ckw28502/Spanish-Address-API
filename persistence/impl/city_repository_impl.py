from persistence.entities.city_entity import CityEntity
from persistence.i_city_repository import ICityRepository


class CityRepositoryImpl(ICityRepository):

    # Get list of cities
    def get_cities(self, city_name) -> list[CityEntity]:
        return list(filter(lambda city: city.get_name == city_name, self._cities))

    # Constructor for the repository
    def __init__(self):
        self._cities = []

    # Checks whether list is empty or not
    def is_empty(self) -> bool:
        return not self._cities

    # Add list of cities to repository's list of cities
    def add_cities(self, addresses: list[CityEntity]) -> None:
        self._cities.extend(addresses)
