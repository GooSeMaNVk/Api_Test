import requests
from data.user_data import RegParam
from data.link import BaseUrl


class Login:
    def false_param(self):
        response = requests.post(BaseUrl().authorization(), data=RegParam().lie_params())
        return response




    def true_param(self):
        response = requests.post(BaseUrl().authorization(), data=RegParam().login())
        return response


