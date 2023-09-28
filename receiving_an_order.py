import requests
import user_data

def all_orders():
    link = "https://stellarburgers.nomoreparties.site/api/orders/all"
    response = requests.get(link)
    assert (response.status_code) == 200
    print(response.json())


def auth_orders():
    param = {"Authorization": user_data.TOKEN}
    link = " https://stellarburgers.nomoreparties.site/api/orders"
    response = requests.get(link, headers=param)
    assert (response.status_code) == 200
    print(response.json())


def uh_orders():
    link = " https://stellarburgers.nomoreparties.site/api/orders"
    response = requests.get(link)
    assert (response.status_code) == 401
    print(response.json())
