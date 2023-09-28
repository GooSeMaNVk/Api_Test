import requests
import user_data


def true_create():
    link = "https://stellarburgers.nomoreparties.site/api/auth/register"
    response = requests.post(link, data=user_data.reg_params)
    assert (response.status_code) == 403
    print(response.json())

def false_create():
    link = "https://stellarburgers.nomoreparties.site/api/auth/register"
    response = requests.post(link, data=user_data.invalid_params)
    assert (response.status_code) == 403
    print(response.json())

def test_with_auth_ing():
    params = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa76",
        ]
    }
    link = "https://stellarburgers.nomoreparties.site/api/orders"
    response = requests.post(link, data=params)
    assert (response.status_code) == 200
    print(response.json()["name"])

