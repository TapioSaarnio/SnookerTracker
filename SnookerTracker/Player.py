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
        self.age = now.year - born.year -((now.month, now.day) < (born.month, born.day))
        self.maxBreaks = data['NumMaximums']

        rankingsRequestUrl = 'http://api.snooker.org/?rt=MoneyRankings&s=' + str(now.year)
        rankingsAnswer = requests.request('GET', rankingsRequestUrl)

        rankings = json.loads(rankingsAnswer.text)
        playersRanking = list(filter(lambda x: (x['PlayerID'] == data['ID']), rankings))
        playersRanking = playersRanking[0]
        self.ranking = playersRanking['Position']

    def printPlayer(self):
        print(self.firstName)