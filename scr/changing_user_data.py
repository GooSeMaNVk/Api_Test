import requests
from data import user_data
from data.link import BaseUrl





def name_change():
    response = requests.patch(BaseUrl().user_change(), headers=user_data.a_token, data={"name": user_data.random_name})
    print("status_code", "=", response.status_code)
    return response.json()['user']['name']



   # response = requests.patch(link, headers=user_data.a_token, data=user_data.random_name)
    #print(response.json()) - можно не делать !
   #def responce ()
    #assert (response.status_code) == 200
    #assert (user_data.random_name) == user_data.random_name


def email_change():
    response = requests.patch(BaseUrl().user_change(), headers=user_data.a_token, data={"email": user_data.random_email})
    print("status_code", "=", response.status_code)
    print(response.json())
    save = response.json()['user']['email']
    data = {"email": save, "password": "password"}
    response2 = requests.post(BaseUrl().authorization(), data=data)
    key = response2.json()["accessToken"]
    token = {"Authorization": key}
    response3 = requests.patch(BaseUrl().user_change(), headers=token, data=user_data.email)
    return response3

def name_change_no_auth():
    response = requests.patch(BaseUrl().authorization(), data=user_data.random_name)
    return response.status_code
