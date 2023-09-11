import requests
import allure

@allure.feature('Изменение_данных_пользователя_Без_авторизации')
def test_run_1():
    PARAM = {"name": "aaa"}
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
    RESPONCE = requests.patch(LINK, data=PARAM)
    assert (RESPONCE.status_code) == (401)
