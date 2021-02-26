"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

"""
MEEETS EXPECTATION CRITERIA:
Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way. - COMPLETE
As a player of the game, I should see a some kind of text header, welcome or game intro message. - COMPLETE
A random number should be chosen that is within the range. - COMPLETE
As a player of the game, I should be continuously prompted for a guess until I get it right. - COMPLETE
As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses. - COMPLETE
As a player of the game, after the game ends I should be shown my number of attempts at guessing. - COMPLETE
When the game ends, an ending message is shown to the player. - COMPLETE

EXCEEDS EXPECTATION CRITERIA:
As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again. -COMPLETE
As a player of the game, after I guess correctly I should be prompted if I would like to play again. - COMPLETE
As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat. - COMPLETE
Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time. -COMPLETE
"""

import random



def start_game():
    print('------------------------------------------------------------')
    print('            WELCOME TO THE NUMBER GUESSING GAME             ')
    print('------------------------------------------------------------')
    print('IN THIS GAME, A NUMBER IN A RANGE WILL BE SELECTED AT RANDOM BETWEEN 1 AND 10.\nYOU WILL TRY TO GUESS THAT NUMBER IN AS LITTLE TRIES AS POSSIBLE.\n')
    high_score = 0
    while True:
        if high_score == False:
            print('\nNO HIGH SCORE HAS BEEN SET.\n')
        else:
            print('\nCURRENT HIGH SCORE IS {}.\n'.format(high_score))
        num = random.randrange(1,11)
        ticker = 1
        print('ENTER A NUMER TO BEGIN...')
        while True:
            try:
                guess = int(input('>> '))
                if guess < 1 or guess > 10:
                    print('THAT NUMBER IS OUTSIDE OF THE RANGE.\nPLEASE ENTER A NEW NUMBER.\n')
                    continue
                if guess < num:
                    print('THE NUMBER IS HIGHER. GUESS AGAIN...\n')
                    ticker += 1
                    continue
                if guess > num:
                    print('THE NUMBER IS LOWER. GUESS AGAIN...\n')
                    ticker += 1
                    continue
                if guess == num:
                    print('YOU GOT IT!\nIT TOOK YOU {} TRIES TO GUESS!\nTHE GAME HAS CONCLUDED.\n'.format(num,ticker))
                    break
                break
            except ValueError:
                print('OOPS! YOU NEED TO ENTER A NUMBER!')
        if high_score == 0 or ticker < high_score:
            high_score = ticker
        replay = input('WOULD YOU LIKE TO PLAY AGAIN?? Y/N  >> ')
        if replay == 'y'.lower():
            continue
        else:
            print('OKAY! GOODBYE.')
            break

start_game()
