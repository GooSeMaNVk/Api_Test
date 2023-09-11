import requests
import user_data


link = "https://stellarburgers.nomoreparties.site/api/auth/register"
response = requests.post(link, data=User_data.reg_params)



print(response.status_code)
response1 = response.json()
print(response1)



# не забываем оставить пустую строку в конце файла