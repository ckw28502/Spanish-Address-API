from persistence.entities.street_entity import StreetEntity
from persistence.i_street_repository import IStreetRepository


class StreetRepositoryImpl(IStreetRepository):
    def get_streets_by_city(self, city) -> list[StreetEntity]:
        return list(filter(lambda street: street.city == city, self._streets))

    def __init__(self):
        self._streets = {}

