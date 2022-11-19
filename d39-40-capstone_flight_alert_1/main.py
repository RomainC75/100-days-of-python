#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

import pprint
pp = pprint.PrettyPrinter(width=50,compact=True)

datamanager:DataManager = DataManager()
today = dt.datetime.now()
depart_from = dt.date.today() + dt.timedelta(days=1)
depart_to = dt.date.today() + dt.timedelta(days=180)
print("departure from : ",depart_from)
print("departure to : ",depart_to)

rows = datamanager.get_rows()


for row in rows['prices']:
    print("==================")
    lowestPrice= row['lowestPrice']
    destination = row['iataCode']
    print("row : ", row)
    flight_search = FlightSearch()
    flight_data = flight_search.check_availaible_flights("PAR", destination, depart_from, depart_to)
    if not flight_data:
        print(f"not direct flight to {destination} found. Try with 2 stops")
        flight_data=flight_search.check_availaible_flights("PAR", destination, depart_from, depart_to, max_stopovers=2)
        pp.pprint(flight_data)

    if flight_data and flight_data.get_data()['price']< lowestPrice:
        notification = NotificationManager(flight_data)
        # notification.send_message()
        notification.send_emails()
        datamanager.update_price(row['id'],flight_data.get_data()['price'])

    if flight_data:
        flight_data.print_data()    
    time.sleep(1)



# flight_search = FlightSearch()
# flight_data=flight_search.check_availaible_flights("PAR", "DPS", depart_from, depart_to, max_stopovers=2)
# print("flight_data : ",flight_data)
# flight_data.print_data()

