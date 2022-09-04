import datetime
from this import d
from threading import local
import requests
import pandas as pd
import json
from dateutil import tz
import pytz
url = 'http://api.snooker.org'


def today ():
    # Returns the games that have been played or will be played today.


    date = datetime.date.today()
    
    print('date on')
    print(date)

    requestStringEventsThisYear = url + "/?t=5&s=[" + str(date.year) + ']'
        
    answerEventsThisYear = requests.request("GET", requestStringEventsThisYear)

    eventsThisYear = json.loads(answerEventsThisYear.text)

    for i in eventsThisYear:
        print(pd.to_datetime(i['StartDate']) <= date and pd.to_datetime(i['EndDate']) >= date)


    eventsNow = list(filter(lambda x: (pd.to_datetime(x['StartDate']) <= date and pd.to_datetime(x['EndDate']) >= date), eventsThisYear)) #every event which StartDate is before current date and EndDate after current date
    matchesOfEventsNow = []

    print('events now')
    print(eventsNow)

    for i in eventsNow:
        requestStringMatchesOfEvent = url + '/?t=6&e=' + str(i['ID'])
        print('requestStringMatchesOfEvent')
        print(requestStringMatchesOfEvent)
        answerMatchesOfAnEvent = requests.request('GET', requestStringMatchesOfEvent)
        matchesOfEventsNow = matchesOfEventsNow + json.loads(answerMatchesOfAnEvent.text)


    print('matches of events now')

    print(matchesOfEventsNow)

    for i in matchesOfEventsNow:
        print('i, startdate')
        print(i['StartDate'])
        if(i['StartDate'].strip()):     #converts timezone only if string is not empty

            i.update({'StartDate': convertTime(pd.to_datetime(i['StartDate']))})

        if(i['EndDate'].strip()):
            i.update({'EndDate:': convertTime(pd.to_datetime(i['EndDate']))})

    finishedMatchesToday = finishedMatchesToday(matchesOfEventsNow)
    

    return ''


#[{"ID": 1299,"Name": "Championship

def convertTime(dttme):
    #converts datetime to finnish time
    
    from_zone = tz.gettz('Etc/GMT+3') #converts to this timezone TODO: create environmental variable determining summer or winter time
    to_zone = tz.gettz('UTC')
    dttme = dttme.replace(tzinfo = from_zone) #tzinfo=from_zone
    newdttme = dttme.astimezone(to_zone)
    #targettimezone Etc/GMT+3
    print('newdttme')
    print(newdttme)

    return newdttme

def updateDataToFinnishTime(matchesOfEventsNow):

    return ''

def finishedMatchesToday(matchesOfEventsNow):
    #tee

    return ''
