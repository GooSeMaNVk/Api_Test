import allure
import requests
import user_data

@allure.feature('Заказ_авторизированного_позьзователя')
def test_orders():
    PARAM = {"Authorization": user_data.TOKEN}
    LINK = " https://stellarburgers.nomoreparties.site/api/orders"
    RESPONCE = requests.get(LINK, headers=PARAM)
    assert (RESPONCE.status_code) == 200
    print(RESPONCE.json())
