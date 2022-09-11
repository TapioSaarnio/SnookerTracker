import requests

class Match:

    def __init__(self, data):

        self.p1 = data['Player1ID']
        self.p2 = data['Player2ID']
        self.score1 = data['Score1']
        self.score2 = data['Score2']
        self.unfinished = data['Unfinished']
        self.winner = data['WinnerID']