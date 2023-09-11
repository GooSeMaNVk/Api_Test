import requests


params = {"ingredients": ["61c0c5a71d1f82001bdaSaa6d"]}
link =("https://stellarburgers.nomoreparties.site/api/orders")
response = requests.post(link,  data=params)


print(response.status_code)
print(response.text)


