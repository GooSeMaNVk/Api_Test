import allure
import create_user

@allure.feature('Создание_пользователя_который_уже_зарегистрирован')
def test_true_create():
    create_user.true_create()


@allure.feature('Создание_пользователя_с_пустым_обязательным_полем')
def test_false_create():
    create_user.false_create()


