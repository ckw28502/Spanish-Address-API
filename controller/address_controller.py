import json

from business.dto.response.get_address_by_city_response import GetAddressByCityResponse
from business.i_address_service import IAddressService
from business.impl.address_service_impl import AddressServiceImpl
from business.dto.request.get_address_by_city_request import GetAddressByCityRequest


class AddressController:

    def __init__(self):
        self.address_service: IAddressService = AddressServiceImpl()

    def get_address_by_city(self, city_name: str) -> str:
        request: GetAddressByCityRequest = GetAddressByCityRequest(city_name=city_name)
        response: GetAddressByCityResponse = self.address_service.get_address_by_city(request)
        json_response: str = json.dumps(response.__dict__)
        return json_response
