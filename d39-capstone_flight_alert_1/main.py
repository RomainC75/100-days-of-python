#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

datamanager:DataManager = DataManager()
today = dt.datetime.now()
depart_from = dt.date.today() + dt.timedelta(days=1)
depart_to = dt.date.today() + dt.timedelta(days=180)
print("departure from : ",depart_from)
print("departure to : ",depart_to)

rows = datamanager.get_rows()

for row in rows['prices']:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("row : ", row)
    lowestPrice= row['lowestPrice']
    destination = row['iataCode']

    flight_search = FlightSearch()
    flight_data = flight_search.check_availaible_flights("PAR", destination, depart_from, depart_to)
    
    if flight_data.get_data()['price']< lowestPrice:
        print(" ================ ")
        print("row : ", row)
        print("flight_data : ",  flight_data.get_data()['price'])
        #update row
        #send
        notification = NotificationManager(flight_data)
        notification.send_message()





