from dataclasses import dataclass


@dataclass
class CityEntity:

    # Constructor for CityEntity
    def __init__(self, id: int, name: str):
        self._name: str = name
        self._id: int = id

    # Getter for city name
    @property
    def get_name(self) -> str:
        return self._name

    # Getter for city id
    @property
    def get_id(self) -> int:
        return self._id
