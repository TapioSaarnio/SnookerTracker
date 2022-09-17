import sys
from Match import Match
import reqs
import requests
import json
def main ():

    #prints basic info about the program
    print('### SnookerTracker ### \n')
    print('         .')
    print('\n')
    print('       ......')
    print('        ....')
    print('         ..')
    print('          .')
    print('\n')
    print('          .')
    print('\n')
    print('\n')
    print('          .')
    print('\n')
    print('\n')
    print('\n')
    print('     .    .     .')
    print('\n')
    print('@Tapio Saarnio \n')
    print('v.1.0 \n')
    print('type \"man\" for instructions \n')

    userInputExit = ''
    #program runs until user types exit
    while userInputExit != 'exit':
        userinput = input('type command: ')
        userinput = userinput.split()
        
        #lower to make input case insensitive
        match userinput[0].lower():

            case 'today':
                print('Todays games \n')
                todaysMatches = reqs.today()

                if(len(todaysMatches[0]) > 0):
                    'Finished matches played today: '
                    for i in todaysMatches[0]:
                        i.printMatch()
                else:
                    'at the moment there are no finished matches played today'

                if(len(todaysMatches[1]) > 0):
                    print('Matches being played right now: ')
                    for i in todaysMatches[1]:
                        i.printMatch()

                if(len(todaysMatches[2]) > 0):
                    print('Upcoming matches: ')
                    for i in todaysMatches[2]:
                        i.printMatch()

            case 'now':
                print('games that are being played right now \n')
                now = reqs.now()

            case 'player':

                if len(userinput) > 2 :

                    player = reqs.player(userinput[1], userinput[2])

                else:
                    print('Wrong input. Syntax for the player command is: player firstname lastname')
                    continue
                print('info about the player \n')

                if(player):
                    player.printPlayer()


            case 'follow':
                print('tunes into a game')
                if(len(userinput) == 2 and userinput[1].isdigit()):
                    match = reqs.matchById(userinput[1])

                

            case 'man':
                sys

            case 'match':

                testmatchAnswer = requests.request('GET', 'http://api.snooker.org/?e=397&r=1&n=5')
                testmatch = list(json.loads(testmatchAnswer.text))
                
                testMatchObj = Match(testmatch[0])
                print('testmatch')
                testMatchObj.printMatch()
                
                #for i in testmatch:
                    #i = Match(i)
                    #print(i)

                #print(testmatch)

                #for i in testmatch:
                    #i.printMatch()


            case 'exit':
                print('thank you for using SnookerTracker!')
                userInputExit = 'exit'


            
            case _ :
                print('Wrong input. Type \"man\" for instructions \n')


    return 0





if __name__ == "__main__":
    main()
