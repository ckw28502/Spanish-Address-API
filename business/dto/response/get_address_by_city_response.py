from dataclasses import dataclass


@dataclass
class GetAddressByCityResponse:
    def __init__(self, street_names: list[str]):
        self.street_names = street_names

