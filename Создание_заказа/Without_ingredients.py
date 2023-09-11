import requests



link =("https://stellarburgers.nomoreparties.site/api/orders")
response = requests.post(link)
print(response.status_code)
print(response.json())



