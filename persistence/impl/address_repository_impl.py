from persistence.entities.address_entity import AddressEntity
from persistence.i_address_repository import IAddressRepository


class AddressRepositoryImpl(IAddressRepository):

    # Constructor for the repository
    def __init__(self):
        self._addresses = []

    # Checks whether list is empty or not
    def is_empty(self) -> bool:
        return not self._addresses

    # Add list of addresses to repository list of addresses
    def add_addresses(self, addresses: list[AddressEntity]) -> None:
        self._addresses.extend(addresses)

    # Get street names based on city names
    def get_addresses_by_city(self, city_name: str) -> list[AddressEntity]:
        filtered_addresses: list[AddressEntity] = list(filter(lambda address: address.get_city_name == city_name,
                                                              self._addresses))
        return filtered_addresses
