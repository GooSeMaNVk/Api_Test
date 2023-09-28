import user_data
import requests


def false_param():
    link = "https://stellarburgers.nomoreparties.site/api/auth/login"
    response = requests.post(link, data=user_data.lie_params)
    assert (response.status_code) == (401)


def true_param():
    link = "https://stellarburgers.nomoreparties.site/api/auth/login"
    response = requests.post(link, data=user_data.params)
    assert (response.status_code) == (200)
