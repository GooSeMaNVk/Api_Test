import requests
import pytest

def test_passing():
    link = ("https://stellarburgers.nomoreparties.site/api/orders/all")
    response = requests.get(link)
    print(response.status_code)
    print(response.json())