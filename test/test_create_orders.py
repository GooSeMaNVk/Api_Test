import allure
import create_orders

@allure.feature('Запрос всех ингридиентов')
def test_all_ing():
    create_orders.all_ing()

@allure.feature('Заказ_авторизованного_пользователя')
def test_auth_ing():
    create_orders.auth_ing()

@allure.feature('С_неверным_хешем_ингредиентов')
def test_false_hash():
    create_orders.false_hash()

@allure.feature('Заказ_без_авторизации')
def test_with_auth():
    create_orders.with_auth_no_ing()

@allure.feature('Без_ингридиентов')
def test_no_ing():
    create_orders.no_ing()