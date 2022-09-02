import datetime
from this import d
import requests
import pandas as pd
import json
url = 'http://api.snooker.org'

def today ():
    # Returns the games that have been played or will be played today.


    date = datetime.datetime.now()
    
    print('date on')
    print(date)

    requeststring = url + "/?t=5&s=[" + str(date.year) + ']'
        
    answer = requests.request("GET", requeststring)

    eventsthisyear = json.loads(answer.text)

    for i in eventsthisyear:
        print(pd.to_datetime(i['StartDate']) < date and pd.to_datetime(i['EndDate']) > date)


    eventsNow = list(filter(lambda x: (pd.to_datetime(x['StartDate']) < date and pd.to_datetime(x['EndDate']) > date), eventsthisyear))
    print(eventsNow)

    return ''


#[{"ID": 1299,"Name": "Championship