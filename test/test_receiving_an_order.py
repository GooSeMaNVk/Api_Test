import allure
import receiving_an_order

@allure.feature('Все_заказы')
def test_all_orders():
    receiving_an_order.all_orders()

@allure.feature('Заказ_авторизированного_позьзователя')
def test_auth_orders():
    receiving_an_order.auth_orders()

@allure.feature('Заказ_неавторизированного_позьзователя')
def test_uh_orders():
    receiving_an_order.uh_orders()