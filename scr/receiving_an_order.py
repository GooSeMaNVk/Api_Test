import requests
from data import user_data
from data.link import BaseUrl

class ReceivingOrders:

    def auth_orders(sefl):
        response = requests.get(BaseUrl().auth_orders(), headers=user_data.a_token)
        return response


    def uh_orders(sefl):
        response = requests.get(BaseUrl().auth_orders())
        return response
