import requests

# Параметры для регистрации
reg_params = {
    "email": "test-dataTest1111121@yandex.ru",
    "password": "password",
    "name": "Username",
}  # Валидные данные

invalid_params = {
    "email": "test-dataTest1111121@yandex.ru",
    "password": "",
    "name": "Username",
}  # Не Валидные

# Параметры для Авторизации
params = {"email": "test-dataTest1111121@yandex.ru", "password": "password"}  # Валидные

lie_params = {
    "email": "test-dataTes@yandex.ru",
    "password": "password123",
}  # С пустым паролем


link = "https://stellarburgers.nomoreparties.site/api/auth/login"
response = requests.post(link, data=params)
response1 = response.json()

TOKEN = response1["accessToken"]  # Получили в переменную а нужное нам значение
R_TOKEN = response1["refreshToken"]
