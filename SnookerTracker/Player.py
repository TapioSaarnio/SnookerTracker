import pandas as pd
import datetime
import requests
import json

class Player:

    def __init__(self, data):

        self.firstName = data['FirstName']
        self.lastName = data['LastName']

        born =  pd.to_datetime(data['Born'])
        now = datetime.date.today()
        self.age = now.year - born.year -((now.month, now.day) < (born.month, born.day)) #if players birthday and month is before current years birthday and month, add 1 to substrasction of the years
        self.nationality = data['Nationality']
        self.rankinTitles = data['NumRankingTitles']
        self.maxBreaks = data['NumMaximums']
        self.ranking = 0
        rankingsRequestUrl = 'http://api.snooker.org/?rt=MoneyRankings&s=' + str(now.year)
        rankingsAnswer = requests.request('GET', rankingsRequestUrl)

        rankings = json.loads(rankingsAnswer.text)
        playersRanking = list(filter(lambda x: (x['PlayerID'] == data['ID']), rankings))
        if len(playersRanking) == 1:

            playersRanking = playersRanking[0]

            self.ranking = playersRanking['Position']

    def printPlayer(self):

        print('Name: ' + self.firstName + ' ' + self.lastName)
        print('Age: ' + str(self.age))
        print('Nationality: ' + self.nationality)
        print('Ranking: ' + str(self.ranking))
        print('Number of ranking titles: ' + str(self.rankinTitles))
        print('Number of maximum breaks: ' +str(self.maxBreaks))
        
    def printName(self):

        print(self.firstName + ' ' + self.lastName, end="")