import requests
import dotenv
config = dotenv.dotenv_values()


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, link, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.link = link

    def get_data(self):
        return{
            "price":self.price ,
            "origin_city":self.origin_city ,
            "origin_airport":self.origin_airport ,
            "destination_city":self.destination_city ,
            "destination_airport":self.destination_airport ,
            "out_date":self.out_date ,
            "return_date":self.return_date ,
            "stop_overs": self.stop_overs,
            "via_city": self.via_city,
            "link": self.link
        }

    def print_data(self):

        print("==>price",self.price)
        print("origin_city : ",self.origin_city)
        print("origin_airport : ",self.origin_airport)
        print("destination_city : ",self.destination_city)
        print("destination_airport : ",self.destination_airport)
        print("out_date : ",self.out_date)
        print("return_date : ",self.return_date)
        print("stop_overs : ", self.stop_overs)
        if len(self.via_city):
            print("via_city : ", self.via_city)
        print("link : ", self.link)

