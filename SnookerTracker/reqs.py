import datetime
from this import d
from threading import local
from time import timezone
import requests
import pandas as pd
import json
import tzlocal
from dateutil import tz
import pytz
import Match
from Player import Player
import Event
import asyncio
url = 'http://api.snooker.org'


def today ():
    # Returns the games that have been played or will be played today.


    date = datetime.date.today()
    

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

    matchesofeventsnowstring = json.dumps(matchesOfEventsNow)
    jsonFile = open('matchesofeventsnow.json', 'w')
    jsonFile.write(matchesofeventsnowstring)
    jsonFile.close()

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

    matchesupcoming = json.dumps(upcomingMatches)
    jsonFile = open('upcomingMatches.json', 'w')
    jsonFile.write(matchesupcoming)
    jsonFile.close()


   
    #todayMatches = finishedMatchesToday + ongoingMatches + upcomingMatches

    todayMatches = []

    todayMatches.append(finishedMatchesToday)
    todayMatches.append(ongoingMatches)
    todayMatches.append(upcomingMatches)

    print('todayMatches')
    print(todayMatches)
    todayMatchesObj = []

    for i in todayMatches:

        matches = []

        if (len(i)>0): 

            for j in i:
                print('j')
                print(j)
                
                matches.append(Match.Match(j))
        
        print('matches')
        print(matches)
        todayMatchesObj.append(matches)
        

    return todayMatchesObj

    

def now():
    #returns matches that are being played now

    ongoingMatchesAnswer = requests.request('GET', url + '/?t=7')
    ongoingMatches = json.loads(ongoingMatchesAnswer.text)

    ongoingMatchesObj = []

    for i in ongoingMatches:
        ongoingMatchesObj = ongoingMatchesObj + Match.Match(i)

    return ongoingMatchesObj


def player(firstName, lastName):

    allPlayersAnswer = requests.request('GET', url + '/?t=10&st=p&s=2022')

    allPlayers = json.loads(allPlayersAnswer.text)


    player = list(filter(lambda x: (x['FirstName'].lower() == firstName.lower() and x['LastName'].lower() == lastName.lower()), allPlayers))

    if (len(player) == 1):

        return Player(player[0])

    return None


#[{"ID": 1299,"Name": "Championship

def convertTime(dttme):
    #converts datetime to finnish time
    
    localtimezone = tzlocal.get_localzone_name()
    
    print('localtimezone')
    print(localtimezone)
    #print('dtutc')
    #print(dtUTC)
    #from_zone = tz.gettz('UTC') #converts to this timezone TODO: create environmental variable determining summer or winter time
    to_zone = tz.gettz(localtimezone)
    newdttme = dttme.astimezone(to_zone)
    #targettimezone Etc/GMT+3


    return newdttme

def updateDataToFinnishTime(matchesOfEventsNow):

    #Convert StartDate and EndDate to finnish times, if slot empty do nothing

    for i in matchesOfEventsNow:
        
        if(i['StartDate'].strip() and i['EndDate'.strip()]):     #converts timezone only if string is not empty

            i.update({'StartDate': str(convertTime(pd.to_datetime(i['StartDate']))), 'EndDate': str(convertTime(pd.to_datetime(i['EndDate'])))})


    return matchesOfEventsNow

def finishedMatchesTodayDef(matchesOfEventsNow):
    #Returns matches that have been played today
    localtimezone = tzlocal.get_localzone_name()
    now = datetime.datetime.now(pytz.timezone(localtimezone))
    
    to_zone = tz.gettz(localtimezone)
    nowTest = pd.to_datetime("2022-09-17T15:10:24Z")

    print('now')
    print(now)

    print('nowtest')
    print(nowTest)

    finishedMatchesToday = list(filter(lambda x: (str(pd.to_datetime(x['StartDate']).date()) == str(now.date()) and now >= pd.to_datetime(x['EndDate'])), matchesOfEventsNow))
    
    return finishedMatchesToday

def upcomingMatchesToday(matchesOfEventsNow):

    now = datetime.datetime.now()
    
    upcomingMatchesTodayList = list(filter(lambda x: (x['StartDate'] == "" and pd.to_datetime(x['ScheduledDate']).date() == now.date()), matchesOfEventsNow))

    return upcomingMatchesTodayList


def playerById(id):

    playerAnswer = requests.request('GET', url + '/?p=' + str(id))


    player = json.loads(playerAnswer.text)


    return Player(player[0])

def matchById(id):

    matchAnswer = requests.request('GET', url + '')
    match = json.loads(matchAnswer.text)
    matchObj = Match(match)
    return matchObj

def EventById(id):

    
    eventanswer = requests.request('GET', url + '?e=' + str(id))
    event = json.loads(eventanswer.text)
    
    if(event[0]):
        return Event.Event(event[0])

async def printSituations(matches):

    for i in matches:
        i.printMatch()
    
    await asyncio.sleep(180)

#async def follow()