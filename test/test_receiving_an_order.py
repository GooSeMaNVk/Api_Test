import allure
from scr.receiving_an_order import ReceivingOrders

@allure.feature('Заказ_авторизированного_позьзователя')
def test_auth_orders():
    ReceivingOrders().auth_orders()
    print(ReceivingOrders().auth_orders().json()['orders'][0]['name'])
    print("Номер заказа", "=", ReceivingOrders().auth_orders().json()['orders'][0]['number'])
    assert ReceivingOrders().auth_orders().status_code == 200


@allure.feature('Заказ_неавторизированного_позьзователя')
def test_uh_orders():
    ReceivingOrders().uh_orders()
    print(ReceivingOrders().uh_orders().json()['message'])
    assert ReceivingOrders().uh_orders().status_code == 401