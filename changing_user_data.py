import requests
import user_data


def name_change():
    headers = {"Authorization": user_data.TOKEN}
    param = {"name": "aaa"}
    link = "https://stellarburgers.nomoreparties.site/api/auth/user"
    response = requests.patch(link, headers=headers, data=param)
    assert (response.status_code) == 200

def email_change():
    headers = {"Authorization": user_data.TOKEN}
    param = {"email": "test-datatest1111121111@yandex.ru"}
    link = "https://stellarburgers.nomoreparties.site/api/auth/user"
    response = requests.patch(link, headers=headers, data=param)
    assert (response.status_code) == 200


def name_change_no_auth():1
    param = {"name": "aaa"}
    link = "https://stellarburgers.nomoreparties.site/api/auth/user"
    response = requests.patch(link, data=param)
    assert (response.status_code) == (401)
