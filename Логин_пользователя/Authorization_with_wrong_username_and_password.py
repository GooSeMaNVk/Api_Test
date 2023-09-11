import requests
import user_data


link = "https://stellarburgers.nomoreparties.site/api/auth/login"

response = requests.post(link, data=User_data.lie_params)




# не забываем оставить пустую строку в конце файла