import allure
import pytest
import requests
from helpers import DataCourier, Courier
from endpoints import Endpoints
from urls import Urls


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе, проверяем ответ и удаляем курьера')
    def test_courier_login_success(self, courier):
        courier_data = courier
        response = Courier().courier_login_in_the_system_and_get_id_courier(courier_data["data"])
        assert response["status_code"] == 200
        assert response.get("id")

    @allure.title('Проверка ошибки при авторизации курьера без заполнения обязательных полей Login/Password')
    @allure.description('''Отправляем запрос на авторизацию в сервисе без заполнения обязательных полей Login/Password
                         и проверяем ответ''')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_login_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title('Проверка ошибки при авторизации курьера с несуществующими данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе с несуществующими данными и проверяем ответ')
    def test_courier_login_without_null_login_failed(self):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=DataCourier.null_data_login)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
    
    def test_courier_login_with_null_login_failed(self):
    #Тест на авторизацию с пустым логином
      response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=DataCourier.null_data_login)
    
    assert response.status_code == 404
    response_data = response.json()
    assert response_data.get("message") == "Учетная запись не найдена"


    def test_courier_login_with_invalid_credentials_failed(self):
    #Тест на авторизацию с некорректными данными
     invalid_data = {
        "login": "invalid_login_12345",
        "password": "invalid_password_12345"
    }
    response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=invalid_data)
    
    response_data = response.json()
    
    assert response.status_code == 404
    assert "Учетная запись не найдена" in response_data.get("message", "")


    def test_courier_login_with_invalid_format_failed(self):
    #Тест на авторизацию с некорректным форматом данных
     invalid_format = "login=test&password=123"  # неправильный формат
    
    response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=invalid_format)
    
    # Проверяем, что API возвращает ошибку валидации
    assert response.status_code in [400, 422] 