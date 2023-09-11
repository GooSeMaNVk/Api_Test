import allure
import requests

@allure.feature('Без_ингридиентов')
def test_with_auth_no_ing():
    LINK = "https://stellarburgers.nomoreparties.site/api/orders"
    RESPONCE = requests.post(LINK)
    assert (RESPONCE.status_code) == 400
    print(RESPONCE.json())
