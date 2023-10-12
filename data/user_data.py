from faker import Faker
import requests
from link import BaseUrl




fake = Faker()
random_name = fake.name()
random_email = fake.email()
random_pass = fake.password()
email = {"email": "test-dataTest11111112@yandex.ru"}
# Параметры для регистрации
class RegParam():
        def reg_params(self): # Валидные данные
                email = random_email
                password = random_pass
                name = random_name
                return {"email": email, "password": password, "name": name}
        def invalid_params(self):
                email = "test-dataTest11111112@yandex.ru"
                password = fake.password
                name = fake.name
                return {"name": name, "password": password, "test-dataTest11111112@yandex.ru": email} # Не Валидные
        def lie_params(self):
                email = fake.email
                password = fake.password
                return {"email": email, "password": password}
 # С пустым паролем
        @staticmethod
        def login():
                data = {"email": "test-dataTest11111112@yandex.ru", "password": "password"}
                return data




#Заранее зарегестрированный пользователь в системе
response = requests.post(BaseUrl().authorization(), data=RegParam().login())
response1 = response.json()
a = response1["accessToken"]
a_token = {"Authorization": a}
print(a_token)


