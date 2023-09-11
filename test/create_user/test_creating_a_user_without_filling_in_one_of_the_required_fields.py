import allure
import requests
import user_data

@allure.feature('Создание_пользователя_с_пустым_обязательным_полем')
def test_create_with():
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/register"
    RESPONCE = requests.post(LINK, data=user_data.invalid_params)
    assert (RESPONCE.status_code) == 403
    print(RESPONCE.json())
