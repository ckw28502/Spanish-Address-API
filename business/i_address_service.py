from abc import ABC, abstractmethod

from business.dto.request.get_address_by_city_request import GetAddressByCityRequest
from business.dto.response.get_address_by_city_response import GetAddressByCityResponse


class IAddressService(ABC):

    @abstractmethod
    def get_address_by_city(self, request: GetAddressByCityRequest) -> GetAddressByCityResponse:
        pass
