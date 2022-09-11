import sys
import reqs
def main ():

    #prints basic info about the program
    print('### SnookerTracker ### \n')
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
                print(reqs.today())

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
                player.printPlayer()


            case 'follow':
                print('tunes into a game')

            case 'man':
                sys

            case 'exit':
                print('thank you for using SnookerTracker!')
                userInputExit = 'exit'


            
            case _ :
                print('Wrong input. Type \"man\" for instructions \n')


    return 0





if __name__ == "__main__":
    main()
