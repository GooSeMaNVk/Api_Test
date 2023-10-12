import allure
from scr import changing_user_data
from data import user_data


@allure.feature('Изменение_Имени')
def test_name_change():
    changing_user_data.name_change()
    assert changing_user_data.name_change() == user_data.random_name

@allure.feature('Изменение_Почты')# !!!! разберись тут!!!
def test_email_change():
    changing_user_data.email_change()
    assert changing_user_data.email_change() == 200


@allure.feature('Изменение_данных_пользователя_Без_авторизации')
def test_name_change_no_auth():
    changing_user_data.name_change_no_auth()
    assert changing_user_data.name_change_no_auth() == 404


