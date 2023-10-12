import requests
from data import user_data
from data.link import BaseUrl
from data.ingridients import Hash


class Orders:
    def all_ing(self):
        responce = requests.get(BaseUrl().ingredients())
        return responce


    def auth_ing(self):
        responce = requests.post(BaseUrl().orders(), headers=user_data.a_token, data=Hash().pass_hash())
        return responce


    def with_auth(self):
        responce = requests.post(BaseUrl().orders(), data=Hash().pass_hash())
        return responce


    def false_hash(self):
        responce = requests.post(BaseUrl().orders(), data=Hash().false_hash())
        return responce


    def no_ing(self):
        responce = requests.post(BaseUrl().orders())
        return responce
