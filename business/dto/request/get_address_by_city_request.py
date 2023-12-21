from dataclasses import dataclass


@dataclass
class GetAddressByCityRequest:
    def __init__(self, city_name: str):
        self.city_name = city_name

    @property
    def get_city_name(self) -> str:
        return self.city_name
