import allure
import requests

@allure.feature('Заказ_без_авторизации')
def test_with_auth_ing():
    PARAMS = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa76",
        ]
    }
    LINK = "https://stellarburgers.nomoreparties.site/api/orders"
    RESPONCE = requests.post(LINK, data=PARAMS)
    assert (RESPONCE.status_code) == 200
    print(RESPONCE.json()["name"])
