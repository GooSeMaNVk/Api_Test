import requests


link = (" https://stellarburgers.nomoreparties.site/api/orders")
response = requests.get(link)
print(response.status_code)
print(response.json())