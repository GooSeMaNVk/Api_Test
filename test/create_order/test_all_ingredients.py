import allure
import requests


@allure.feature('Запрос всех ингридиентов')
def test_all_ing():
    LINK = " https://stellarburgers.nomoreparties.site/api/ingredients"
    RESPONCE = requests.get(LINK)
    print(RESPONCE.json())
    assert (RESPONCE.status_code) == 200
