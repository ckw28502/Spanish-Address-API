from dataclasses import dataclass


@dataclass
class AddressEntity:

    # Constructor for AddressEntity
    def __init__(self, city_name: str, street_name: str):
        self._city_name: str = city_name
        self._street_name: str = street_name

    # Getter for city name
    @property
    def get_city_name(self) -> str:
        return self._city_name

    # Getter for street name
    @property
    def get_street_name(self) -> str:
        return self._street_name
