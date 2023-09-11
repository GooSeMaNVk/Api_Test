import requests
import user_data


#class TestWith:
#    def test_run(Self):
        Self.HEADERS = {'Authorization': user_data.TOKEN}
        Self.PARAM = {'name': 'aaa'}
        Self.LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
        Self.RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)
        assert (Self.RESPONCE.status_code) == 200
#    def test_run1(Self):
        Self.HEADERS = {'Authorization': user_data.TOKEN}
        Self.PARAM = {'email': 'test-datatest11111211@yandex.ru'}
        Self.LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
        Self.RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)
        assert (Self.RESPONCE.status_code) == 200


#HEADERS = {'Authorization': user_data.TOKEN}
PARAM = {'email': 'test-datatest1111121@yandex.ru'}
LINK = "https://stellarburgers.nomoreparties.site/api/auth/user"
RESPONCE = requests.patch(LINK, headers=HEADERS, data=PARAM)