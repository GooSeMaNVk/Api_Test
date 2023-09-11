import allure
import requests
import user_data

@allure.feature('Заказ_авторизованного_пользователя')
def test_auth_ing():
    HEADERS = {"Authorization": user_data.TOKEN}
    PARAMS = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa76",
        ]
    }
    LINK = "https://stellarburgers.nomoreparties.site/api/orders"
    RESPONCE = requests.post(LINK, headers=HEADERS, data=PARAMS)
    assert (RESPONCE.status_code) == 200
    print(RESPONCE.json()["name"])
