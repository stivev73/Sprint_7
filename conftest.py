import pytest

from helpers import Courier


# фикстура регистрации, авторизации и удаления курьера
@pytest.fixture()
def courier():
    # Только создает курьера и возвращает данные
    courier_data = Courier().courier_registration_in_the_system_and_get_courier_data()
    yield courier_data
    # После теста удаляем курьера
    Courier().courier_subsequent_deletion(courier_data["id"])


@pytest.fixture()
def courier_login(courier):
    # Выполняет авторизацию уже созданного курьера
    login_data = Courier().courier_login_in_the_system_and_get_id_courier(courier["data"])
    return login_data

# фикстура регистрации, авторизации и удаления курьера
@pytest.fixture()
def courier_delete():
    courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
    courier_login = Courier().courier_login_in_the_system_and_get_id_courier(courier_create["data"])
    yield courier_login