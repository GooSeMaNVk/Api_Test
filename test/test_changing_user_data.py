import allure
import changing_user_data


@allure.feature('Изменение_Имени')
def test_name_change():
    changing_user_data.name_change()
@allure.feature('Изменение_Почты')
def test_email_change():
    changing_user_data.email_change()


@allure.feature('Изменение_данных_пользователя_Без_авторизации')
def test_name_change_no_auth():
    changing_user_data.name_change_no_auth()


