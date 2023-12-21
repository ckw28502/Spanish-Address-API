from flask import Flask

from controller.address_controller import AddressController

app = Flask(__name__)

addressController: AddressController = AddressController()


@app.route('/<string:city_name>', methods=['GET'])
def get_addresses_by_city(city_name: str):
    return addressController.get_address_by_city(city_name)


if __name__ == '__main__':
    app.run()
