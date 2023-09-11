import allure
import requests

@allure.feature('Все_заказы')
def test_all_orders():
    LINK = "https://stellarburgers.nomoreparties.site/api/orders/all"
    RESPONCE = requests.get(LINK)
    assert (RESPONCE.status_code) == 200
    print(RESPONCE.json())
