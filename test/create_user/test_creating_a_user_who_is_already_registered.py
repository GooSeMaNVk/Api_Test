import allure
import requests
import user_data

@allure.feature('Создание_пользователя_который_уже_зарегистрирован')
def test_create():
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/register"
    RESPONCE = requests.post(LINK, data=user_data.reg_params)
    assert (RESPONCE.status_code) == 403
    print(RESPONCE.json())



