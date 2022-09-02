import sys
import reqs
def main ():

    #prints basic info about the program
    print('### SnookerTracker ### \n')
    print('@Tapio Saarnio \n')
    print('v.1.0 \n')
    print('type \"man\" for instructions \n')

    userinput = ''
    #program runs until user types exit
    while userinput != 'exit':
        userinput = input('type command: ')
        
        #lower to make input case insensitive
        match userinput.lower():

            case 'today':
                print('Todays games \n')
                print(reqs.today())

            case 'now':
                print('games that are being played right now \n')

            case 'player':
                print('info about the player \n')

            case 'follow':
                print('tunes into a game')

            case 'man':
                sys

            case 'exit':
                print('thank you for using SnookerTracker!')

            
            case _ :
                print('Wrong input. Type \"man\" for instructions \n')


    return 0





if __name__ == "__main__":
    main()
