import datetime as dt
import requests
import dotenv
config = dotenv.dotenv_values()
import json

#==========================================
# this script asks what kind of exercice you did today in a natural language
# and it write it down to a google sheet
# uses 2 apis : sheety(connected to google sheet) and nutritionix

key=config['NUTRITIONIX_KEY']
id = config["NUTRITIONIX_APP_ID"]
BEARER = config["SHEETY_BEARER"]

headers={
    "x-app-id":id,
    "x-app-key":key,
    "x-remote-user-id":"0"
}

nutrients_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint="https://api.sheety.co/6a5c5ac0fcac8b7574d0f2b93b8f2e29/workoutTracking/sheet1"


natural_text = input("what did you do ? ")

req_data={
    "query":natural_text,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}

raw = requests.post(nutrients_endpoint,json=req_data,headers=headers)
raw.raise_for_status()

nutritionix_ans = raw.json()
now = dt.datetime.now()

#sheety 
def add_new_line(exo):

    print("==> ", exo['name'],exo['duration_min'], exo['nf_calories'])
    print(now.strftime("%d/%m/%Y"), now.strftime("%H:%M:%S"))

    body = {
        "sheet1": {
            "date":now.strftime("%d/%m/%Y"),
            "time":now.strftime("%H:%M:%S"),
            "exercise":exo['name'],
            "duration":exo['duration_min'], 
            "calories":exo['nf_calories']
        }
    }
    headers={
        "Authorization":f"Bearer {BEARER}"
    }
    ans_raw = requests.post(sheety_endpoint, json=body, headers=headers)
    print("=>", ans_raw)


for exo in nutritionix_ans['exercises']:
    add_new_line(exo)