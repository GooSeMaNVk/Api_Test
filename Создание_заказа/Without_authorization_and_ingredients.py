import requests

params = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa72","61c0c5a71d1f82001bdaaa76"]
}
link =("https://stellarburgers.nomoreparties.site/api/orders")
response = requests.post(link,  data=params)
response1 = response.json()
order = (response1['order'])
print(response.status_code)
print(response.json())

print(order)

