import requests

params = {'Authorization': User_data.A_Token}
link = (" https://stellarburgers.nomoreparties.site/api/orders")
response = requests.get(link, headers=params)
print(response.status_code)
print(response.json())