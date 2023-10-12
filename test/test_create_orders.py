import allure
from scr.create_orders import Orders

@allure.feature('Запрос всех ингридиентов')
def test_all_ing():
    print(Orders().all_ing().json())
    assert Orders().all_ing().status_code == 200

@allure.feature('Заказ_авторизованного_пользователя')
def test_auth_ing():
    print(Orders().auth_ing().json()["name"])
    print(Orders().auth_ing().json()["order"])
    assert Orders().auth_ing().status_code == 200

@allure.feature('С_неверным_хешем_ингредиентов')
def test_false_hash():
    print(Orders().false_hash().text)
    assert Orders().false_hash().status_code == 500


@allure.feature('Заказ_без_авторизации')
def test_with_auth():
    print(Orders().with_auth().json()["name"], Orders().with_auth().json()["order"])
    assert Orders().with_auth().status_code == 200

@allure.feature('Без_ингридиентов')
def test_no_ing():
    print(Orders().no_ing().json()["message"])
    assert Orders().no_ing().status_code == 400
