from business.dto.request.get_address_by_city_request import GetAddressByCityRequest
from business.dto.response.get_address_by_city_response import GetAddressByCityResponse
from business.i_address_service import IAddressService
from persistence.entities.address_entity import AddressEntity
from persistence.i_address_repository import IAddressRepository
from persistence.impl.address_repository_impl import AddressRepositoryImpl


class AddressServiceImpl(IAddressService):

    # Constructor
    def __init__(self):
        self._address_repository: IAddressRepository = AddressRepositoryImpl()

    def get_address_by_city(self, request: GetAddressByCityRequest) -> GetAddressByCityResponse:

        if self._address_repository.is_empty():
            self.__read_shape_file()

        addresses: list[AddressEntity] = self._address_repository.get_addresses_by_city(request.get_city_name)
        street_names: list[str] = list(address.get_street_name for address in addresses)
        response: GetAddressByCityResponse = GetAddressByCityResponse(street_names=street_names)
        return response

    # Read the shape file
    # TODO
    def __read_shape_file(self):
        self._address_repository.add_addresses([AddressEntity("Surabaya","Lontar")])