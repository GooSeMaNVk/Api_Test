import allure
import requests
import user_data

@allure.feature('Авторизация_с_валидными_данными')
def test_run3():
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/login"
    RESPONCE = requests.post(LINK, data=user_data.params)
    assert (RESPONCE.status_code) == (200)
