import requests
import user_data

HEADERS = {'Authorization': user_data.TOKEN}
PARAMS = {'name': 'aaa'}
LINK ="https://stellarburgers.nomoreparties.site/api/auth/user"
RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAMS)

print(RESPONCE)
print(RESPONCE.text)

PARAMS = {'email': 'test-datatest11111211@yandex.ru'}
LINK ="https://stellarburgers.nomoreparties.site/api/auth/user"
RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAMS)

print(RESPONCE)
print(RESPONCE.text)


PARAMS = {'email': 'test-datatest1111121@yandex.ru'}
LINK ="https://stellarburgers.nomoreparties.site/api/auth/user"
RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAMS)