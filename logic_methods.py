import allure
from faker import Faker
import requests

from endpoints import Endpoints
from urls import Urls

class Courier:

    # функция регистрации в системе с возвратом ответа и данных курьера
    @allure.step
    @staticmethod
    def courier_registration_in_the_system_and_get_courier_data():
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    # функция логина в системе с возвратом ответа и id курьера
    @allure.step
    @staticmethod
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    # функция удаления курьера
    @allure.step
    @staticmethod
    def courier_subsequent_deletion(id):
        response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{id}')
        return {"response_text": response.text, "status_code": response.status_code}