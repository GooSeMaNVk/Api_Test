import allure
import requests
import user_data


@allure.feature('Изменение_Имени')
def test_run():
    HEADERS = {"Authorization": user_data.TOKEN}
    PARAM = {"name": "aaa"}
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
    RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)
    assert (RESPONCE.status_code) == 200

@allure.feature('Изменение_Почты')
def test_run1():
    HEADERS = {"Authorization": user_data.TOKEN}
    PARAM = {"email": "test-datatest111112111@yandex.ru"}
    LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
    RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)
    assert (RESPONCE.status_code) == 200


HEADERS = {"Authorization": user_data.TOKEN}
PARAM = {"email": "test-datatest1111121@yandex.ru"}
LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)
