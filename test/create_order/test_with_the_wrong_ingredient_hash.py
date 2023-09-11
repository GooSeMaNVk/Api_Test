import allure
import requests

@allure.feature('С_неверным_хешем_ингредиентов')
def test_fail_hash():
    PARAMS = {"ingredients": ["61c0c5a71d1f82001bdaSaa6d"]}
    LINK = "https://stellarburgers.nomoreparties.site/api/orders"
    RESPONE = requests.post(LINK, data=PARAMS)
    assert (RESPONE.status_code) == 500
    print(RESPONE.text)
