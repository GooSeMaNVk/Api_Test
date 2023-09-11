import requests


params = {'name': 'aaa'}
link ="https://stellarburgers.nomoreparties.site/api/auth/user"
response = requests.patch(link, data=params)

print(response)
print(response.text)