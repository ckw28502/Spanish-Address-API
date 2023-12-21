from abc import ABC, abstractmethod

from persistence.entities.address_entity import AddressEntity


class IAddressRepository(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add_addresses(self, addresses: list[AddressEntity]) -> None:
        pass

    @abstractmethod
    def get_addresses_by_city(self, city_name: str) -> list[AddressEntity]:
        pass
