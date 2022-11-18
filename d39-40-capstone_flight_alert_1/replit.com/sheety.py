import requests
import dotenv
config = dotenv.dotenv_values()

class Sheety:
  def __init__(self) -> None:
    self.api_url = "https://api.sheety.co/6a5c5ac0fcac8b7574d0f2b93b8f2e29/flightDestination/users"
    self.headers = {"Authorization": f'Bearer {config["SHEETY_BEARER"]}'}

  def post_new_user(self, first_name, last_name, email):
    body = {"user":{"firstName": first_name, "lastName": last_name, "email": email}}
    raw_ans = requests.post(url=self.api_url, headers=self.headers, json=body)
    raw_ans.raise_for_status()
    # ans = raw_ans.json()

