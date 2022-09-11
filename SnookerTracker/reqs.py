import datetime
from this import d
from threading import local
import requests
import pandas as pd
import json
from dateutil import tz
import pytz
import Match
from Player import Player
url = 'http://api.snooker.org'


def today ():
    # Returns the games that have been played or will be played today.


    date = datetime.date.today()
    
    print('date on')
    print(date)

    requestStringEventsThisYear = url + "/?t=5&s=[" + str(date.year) + ']'
        
    answerEventsThisYear = requests.request("GET", requestStringEventsThisYear)  #Get events taking place this year

    eventsThisYear = json.loads(answerEventsThisYear.text)

    eventsNow = list(filter(lambda x: (pd.to_datetime(x['StartDate']) <= date and pd.to_datetime(x['EndDate']) >= date), eventsThisYear)) #every event which StartDate is before current date and EndDate after current date
    matchesOfEventsNow = []

    print('events now')
    print(eventsNow)

    for i in eventsNow:                                                              #Get every match of every event going on now
        requestStringMatchesOfEvent = url + '/?t=6&e=' + str(i['ID'])
        print('requestStringMatchesOfEvent')
        print(requestStringMatchesOfEvent)
        answerMatchesOfAnEvent = requests.request('GET', requestStringMatchesOfEvent)
        matchesOfEventsNow = matchesOfEventsNow + json.loads(answerMatchesOfAnEvent.text)


    print('matches of events now')

    print(matchesOfEventsNow)

    
    matchesOfEventsNow = updateDataToFinnishTime(matchesOfEventsNow)               #convert to etc+2 or etc+3

    print('matches of events now UPDATED')

    print(matchesOfEventsNow)

    finishedMatchesToday = finishedMatchesTodayDef(matchesOfEventsNow)
    ongoingMatchesAnswer = requests.request('GET', url + '/?t=7')
    ongoingMatches = list(json.loads(ongoingMatchesAnswer.text))
    upcomingMatches = upcomingMatchesToday(matchesOfEventsNow)
    
    print('finishedMatchesToday')

    print(finishedMatchesToday)

    print('ongoingmatches')
    print(ongoingMatches)
    print('upcomingmatches')
    print(upcomingMatches)

    todayMatches = finishedMatchesToday + ongoingMatches + upcomingMatches

    print('todayMatches')
    print(todayMatches)

    todayMatchesObj = []

    for i in todayMatches:

        todayMatchesObj = todayMatchesObj + Match(i)

    return todayMatchesObj





def now():
    #returns matches that are being played now

    ongoingMatchesAnswer = requests.request('GET', url + '/?t=7')
    ongoingMatches = json.loads(ongoingMatchesAnswer.text)

    ongoingMatchesObj = []

    for i in ongoingMatches:
        ongoingMatchesObj = ongoingMatchesObj + Match(i)

    return ongoingMatchesObj


def player(firstName, lastName):

    print('firstname lastname')
    print(firstName)
    print(lastName)
    allPlayersAnswer = requests.request('GET', url + '/?t=10&st=p&s=2022')

    allPlayers = json.loads(allPlayersAnswer.text)

    print('allplayers')
    print(allPlayers)

    player = list(filter(lambda x: (x['FirstName'] == firstName and x['LastName'] == lastName), allPlayers))
    print('player')
    print(player[0])

    if (player[0]):

        return Player(player[0])

    return None


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

    #Convert StartDate and EndDate to finnish times, if slot empty do nothing

    for i in matchesOfEventsNow:
        print('i, startdate')
        print(i['StartDate'])
        if(i['StartDate'].strip()):     #converts timezone only if string is not empty

            i.update({'StartDate': convertTime(pd.to_datetime(i['StartDate']))})

        if(i['EndDate'].strip()):
            i.update({'EndDate:': convertTime(pd.to_datetime(i['EndDate']))})

    return matchesOfEventsNow

def finishedMatchesTodayDef(matchesOfEventsNow):
    #Returns matches that have been played today
    
    now = datetime.datetime.now()
    nowTest = pd.to_datetime("2022-09-09T15:10:24Z")

    print('nowTest')
    print(nowTest.date() == now.date())
    finishedMatchesToday = list(filter(lambda x: (pd.to_datetime(x['StartDate']).date() == now.date() and now >= pd.to_datetime(x['EndDate'])), matchesOfEventsNow))
    
    return finishedMatchesToday

def upcomingMatchesToday(matchesOfEventsNow):

    now = datetime.datetime.now()
    
    upcomingMatchesTodayList = list(filter(lambda x: (pd.to_datetime(x['StartDate']).date() == "" and pd.to_datetime(x['ScheduledDate']).date() == now.date()), matchesOfEventsNow))

    return upcomingMatchesTodayList
    