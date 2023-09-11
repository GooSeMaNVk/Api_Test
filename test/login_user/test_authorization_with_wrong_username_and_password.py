import allure
import requests
import user_data

@allure.feature('Авторизация_с_неверным_логином_и_паролем')
def test_run2():
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/login"
    RESPONCE = requests.post(LINK, data=user_data.lie_params)
    assert (RESPONCE.status_code) == (401)
