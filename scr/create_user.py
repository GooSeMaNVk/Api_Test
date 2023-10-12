import requests

link = "https://stellarburgers.nomoreparties.site/api/auth/register"

class Token:
    token = None
    user_data = str()
    @staticmethod
    def tokens():
        token = Login.true_param(Login)
        return token

class Login:
    def true_param(self):

       self.token = s_token
       self.user_data = a
       return self.user_data, self.token
 #   def test_true_create(self, token):
 #       data = user_data.reg_params()
    #    response = requests.post(link, data=data)
   #     assert (response.status_code) == 200a
  #      print(response.json())
  #      s_token = response["accessToken"]
  #      a = response["email", "password"]
   #     self.token = s_token
  #      self.user_data = a
  #      return self.user_data, self.token




    def test_false_create(fail):
        data = user_data.invalid_params()
        response = requests.post(link, data=data)
        assert (response.status_code) == 403
        assert response.json().get('message') == 'Email, password and name are required fields'
        print(response.json())



