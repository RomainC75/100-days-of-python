import requests
from flight_data import FlightData
import dotenv
config = dotenv.dotenv_values()

URL = "https://siddiq-such-flight-v1.p.rapidapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key=config['TEQUILA_KEY']
        self.headers={
            'accept': 'application/json',
            'apikey': self.api_key
        }
        self.api_url="https://api.tequila.kiwi.com"
        
    def get_iata_code(self, name):
        endpoint="locations/query"
        params={
            "term":name,
            "locale":"en-US",
            "location_types":"city",
            "limit":10,
            "active_only":True
        }        
        raw_ans = requests.get(f"{self.api_url}/{endpoint}",params=params,headers=self.headers)
        res = raw_ans.json()
        return res['locations'][0]['code']
    
    def check_availaible_flights(self, from_city_code, to_city_code, from_time, to_time):
        endpoint="v2/search"
        params = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        raw_ans = requests.get( f'{self.api_url}/{endpoint}', params=params, headers=self.headers )
        raw_ans.raise_for_status()
        ans = raw_ans.json()
        route = ans['data'][0]['route'][0]

        flight_data = FlightData(
            price = ans['data'][0]['price'],
            out_date = ans['data'][0]['route'][0]['local_departure'],
            return_date = ans['data'][0]['route'][1]['local_departure'],
            origin_city= route['cityFrom'],
            origin_airport=route['flyFrom'],
            destination_city=route['cityTo'],
            destination_airport=route['flyTo']
        )
        return flight_data
        