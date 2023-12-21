from abc import ABC, abstractmethod

from persistence.entities.street_entity import StreetEntity


class IStreetRepository(ABC):

    @abstractmethod
    def get_streets_by_city(self, city) -> list[StreetEntity]:
        pass
