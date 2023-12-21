from flask import Flask, jsonify, Response

from business.dto.exception.custom_exception import CustomException
from controller.address_controller import AddressController

app = Flask(__name__)

addressController: AddressController = AddressController()


@app.route('/<string:city_name>', methods=['GET'])
def get_addresses_by_city(city_name: str):
    return addressController.get_address_by_city(city_name)


@app.errorhandler(CustomException)
def custom_exception(error: CustomException):
    status: str= "BAD_REQUEST" if error.status_code == 400 else "INTERNAL_SERVER_ERROR"
    response: Response = jsonify({"status": status,"code": error.status_code, "message": str(error)})
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
