import allure
import login


@allure.feature('Авторизация_с_неверным_логином_и_паролем')
def test_false_param():
    login.false_param()
    return test_true_param == 300


@allure.feature('Авторизация_с_валидными_данными')
def test_true_param():
    login.true_param()
