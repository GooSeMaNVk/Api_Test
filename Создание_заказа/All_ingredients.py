import requests

link = (" https://stellarburgers.nomoreparties.site/api/ingredients")
response = requests.get(link)
print(response.json())
response1 = response.json()
a = (response1['data']['id'][0])
print(a)