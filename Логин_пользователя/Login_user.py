import requests

link = "https://stellarburgers.nomoreparties.site/api/auth/login"

response = requests.post(link, data=User_data.params)



print(response.status_code)
print(response.text)


# не забываем оставить пустую строку в конце файла
