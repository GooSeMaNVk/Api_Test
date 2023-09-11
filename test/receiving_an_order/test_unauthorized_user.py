import allure
import requests

@allure.feature('Заказ_неавторизированного_позьзователя')
def test_orders_1():
    LINK = " https://stellarburgers.nomoreparties.site/api/orders"
    RESPONCE = requests.get(LINK)
    assert (RESPONCE.status_code) == 401
    print(RESPONCE.json())
