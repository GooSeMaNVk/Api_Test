import allure
from scr.login import Login


@allure.feature('Авторизация_с_неверным_логином_и_паролем')
def test_false_param():
    print(Login().false_param().json()['message'])
    assert Login().false_param().status_code == 401


@allure.feature('Авторизация_с_валидными_данными')
def test_true_param():
    print(Login().true_param().json()['success'], "-", "Успешно")
    assert (Login().true_param().status_code) == (200)

