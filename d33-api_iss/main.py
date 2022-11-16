import requests
import pprint
from datetime import datetime
# ans = requests.get("http://api.open-notify.org/iss-now.json")
# #raise error 
# ans.raise_for_status()

# data = ans.json()
# print("data : ",data)

coord={
    "lat":48.856613,
    "lng":2.352222,
    "formatted":0
}

raw_ans = requests.get(f"https://api.sunrise-sunset.org/json", params=coord)
raw_ans.raise_for_status()
data = raw_ans.json()

sunrise_hour = data['results']['sunrise'].split("T")[1]
sunrise_hour =  sunrise_hour.split(":")[0]
print("sunrise : ",sunrise_hour)

sunset_hour = data['results']['sunset'].split("T")[1]
sunset_hour = sunset_hour.split(":")[0]
print("sunset : ",sunset_hour)

time_now = datetime.now().hour
print(time_now)