import unittest
from unittest.mock import patch
from business.dto.request.get_address_by_city_request import GetAddressByCityRequest
from business.dto.response.get_address_by_city_response import GetAddressByCityResponse
from business.i_address_service import IAddressService
from business.impl.address_service_impl import AddressServiceImpl
from persistence.entities.city_entity import CityEntity
from persistence.entities.street_entity import StreetEntity


class TestAddressServiceImpl(unittest.TestCase):

    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.get_cities_by_name')
    @patch('persistence.impl.street_repository_impl.StreetRepositoryImpl.get_streets_by_city')
    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.is_empty')
    def test_get_address_by_city_one_city_no_streets(self, mock_is_empty, mock_get_streets, mock_get_cities):

        # Arrange

        address_service: IAddressService = AddressServiceImpl()

        request = GetAddressByCityRequest(city_name='City1')

        mock_is_empty.return_value = False

        city: CityEntity = CityEntity(id=1, name='City1')

        mock_get_cities.return_value = [city]

        streets: list[StreetEntity] = [StreetEntity(id=1, name='Street1', city=city),
                                       StreetEntity(id=2, name='Street2', city=city)]

        mock_get_streets.return_value = streets

        street_names = [street.get_name for street in streets]

        expected_response: GetAddressByCityResponse = GetAddressByCityResponse(street_names=street_names)

        # Act
        actual_response: GetAddressByCityResponse = address_service.get_address_by_city(request)

        # Assert
        self.assertEqual(expected_response, actual_response)

    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.get_cities_by_name')
    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.is_empty', return_value=False)
    def test_get_address_by_city_multiple_cities(self, mock_is_empty, mock_get_cities):

        # Arrange
        address_service = AddressServiceImpl()

        request = GetAddressByCityRequest(city_name='City1')

        mock_get_cities.return_value = [CityEntity(id=1, name='City1'), CityEntity(id=2, name='City2')]

        # Act
        with self.assertRaises(Exception) as context:
            address_service.get_address_by_city(request)

        # Assert
        self.assertEqual(str(context.exception), "MORE THAN ONE CITY IS FOUND!")

    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.get_cities_by_name')
    @patch('persistence.impl.city_repository_impl.CityRepositoryImpl.is_empty', return_value=False)
    def test_get_address_by_city_no_cities(self, mock_is_empty, mock_get_cities):
        # Arrange
        address_service = AddressServiceImpl()

        request = GetAddressByCityRequest(city_name='City1')

        mock_get_cities.return_value = []

        # Act
        with self.assertRaises(Exception) as context:
            address_service.get_address_by_city(request)

        # Assert
        self.assertEqual(str(context.exception), "CITY NOT FOUND!")


if __name__ == '__main__':
    unittest.main()
