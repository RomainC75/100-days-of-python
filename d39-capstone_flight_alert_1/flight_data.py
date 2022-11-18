import requests
import dotenv
config = dotenv.dotenv_values()


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def get_data(self):
        return{
            "price":self.price ,
            "origin_city":self.origin_city ,
            "origin_airport":self.origin_airport ,
            "destination_city":self.destination_city ,
            "destination_airport":self.destination_airport ,
            "out_date":self.out_date ,
            "return_date":self.return_date 
        }

        

