from persistence.entities.street_entity import StreetEntity
from persistence.i_street_repository import IStreetRepository


class StreetRepositoryImpl(IStreetRepository):

    # Method to add streets to list of streets in repository
    def add_streets(self, streets: list[StreetEntity]) -> None:
        self._streets.extend(streets)

    # Method to get streets by city name
    def get_streets_by_city(self, city) -> list[StreetEntity]:
        return list(filter(lambda street: street.get_city == city, self._streets))

    # Constructor
    def __init__(self):
        self._streets = []

