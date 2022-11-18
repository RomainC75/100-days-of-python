import requests
import dotenv
config = dotenv.dotenv_values()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.url="https://api.sheety.co/6a5c5ac0fcac8b7574d0f2b93b8f2e29/flightDestination/prices"
        self.headers = {
            "Authorization":f'Bearer {config["SHEETY_BEARER"]}'
        }
        
    def get_rows(self):
        raw_ans=requests.get(self.url, headers=self.headers)
        # print("raw : ", raw_ans.text)
        ans = raw_ans.json()
        return ans
        
    def get_row(self, destination:str):
        body = {
            "price":{
                "city":destination.title(),
            }
        }
        new_url=f'{self.url}?filter[city]={destination}'
        raw_ans = requests.get(new_url, headers=self.headers)
        return raw_ans.json()


    def update_IATA_codes(self):
        rows = self.get_rows()
        print("pre : ", rows)
        for row in rows['prices']:
            print("=>",row)
            if len(row['iataCode'])==0:
                print("...",row['id'], row['city'].replace(" ","")[0:3].upper() )
                self.update_IATA_code( row['id'], row['city'].replace(" ","")[0:3].upper() )

    def update_IATA_code(self,id,iata):
        body = {
            "price":{
                "iataCode":iata
            }
        }
        raw_ans = requests.put(f'{self.url}/{id}', json=body, headers=self.headers)
        print(f'put iata : {id}', raw_ans)

    def update_price(self,id, new_price:int):
        body = {
            "price":{
                "lowestPrice":new_price
            }
        }
        raw_ans = requests.put(f'{self.url}/{id}', json=body, headers=self.headers)
        print(f'put iata : {id}', raw_ans)
        