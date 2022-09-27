import requests
import reqs
from Player import Player
from Event import Event

class Match:

    def __init__(self, data):

        self.id = data['ID']
        self.p1 = reqs.playerById(data['Player1ID'])
        self.p2 = reqs.playerById(data['Player2ID'])
        self.score1 = data['Score1']
        self.score2 = data['Score2']
        self.unfinished = data['Unfinished']
        self.onBreak = data['OnBreak']
        winnerOfTheGame = data['WinnerID']
        self.event = reqs.EventById(data['EventID'])

        if(winnerOfTheGame !=0):
            
            self.winner = reqs.playerById(data['WinnerID'])

        else:
            self.winner = None


    def printMatch(self):

        
        self.event.printEvent()
        self.p1.printName()
        print(' vs ', end="")
        self.p2.printName()
        print('\n')
        print('     ' + str(self.score1) + '    Frames   ' + str(self.score2))

        if(self.onBreak):
            print('Match is on break')

        if(self.unfinished):
            print('  Match is unfinished')


        if(self.winner):

             print('Winner: ', end=' ')
             self.winner.printName()

        print('  id: ' + str(self.id))
        print('\n')
        print('..........................')

    def printSituation(self):

        self.p1.printName()
        print(' vs ', end="")
        self.p2.printName()
        print('\n')
        print('     ' + str(self.score1) + '    Frames   ' + str(self.score2)) 

        print('-----------------------------------')

        