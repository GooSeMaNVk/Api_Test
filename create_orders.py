import requests
import user_data



def all_ing():
    link = " https://stellarburgers.nomoreparties.site/api/ingredients"
    responce = requests.get(link)
    print(responce.json())
    assert (responce.status_code) == 200

def auth_ing():
    headers = {"Authorization": user_data.TOKEN}
    params = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa76",
        ]
    }
    link = "https://stellarburgers.nomoreparties.site/api/orders"
    responce = requests.post(link, headers=headers, data=params)
    assert (responce.status_code) == 200
    print(responce.json()["name"])


def false_hash():
    params = {"ingredients": ["61c0c5a71d1f82001bdaSaa6d"]}
    link = "https://stellarburgers.nomoreparties.site/api/orders"
    responce = requests.post(link, data=params)
    assert (responce.status_code) == 500
    print(responce.text)


def with_auth():
    params = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa76",
        ]
    }
    link = "https://stellarburgers.nomoreparties.site/api/orders"
    responce = requests.post(link, data=params)
    assert (responce.status_code) == 400
    print(responce.json())

def no_ing():
    link = "https://stellarburgers.nomoreparties.site/api/orders"
    responce = requests.post(link)
    assert (responce.status_code) == 400
    print(responce.json())