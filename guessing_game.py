"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
---------------------------------
"""
"""
Project Primary Goals:
----------------
1. Make sure script runs without errors or unhandled expceptions.
2. Provide intro/welcome message to user
3. Choose randon number in a range (1-10)
4. Continuously prompt user for a guess until they get it correct
5. Provide feedback to incorrect guesses ("higher"/"lower")
6. Once user gets correct answer, display number of guesses they took
7. Provide ending message to user

Extra Credit Goals:
-------------------
1. Provide feedback to user if their guess is outside the 1-10 range. Prompt to try again.
2. Ask player if they would like to play again after completing the game.
3. Store a high score (lower number of tries) and display to user at start of each game
4. Make sure number is updated at start of each game if user chooses to play again.


"""

import random



def start_game():
    print('-------------------------------------------------------------------------------')
    print('                      WELCOME TO THE NUMBER GUESSING GAME                      ')
    print('-------------------------------------------------------------------------------')
    print('IN THIS GAME, A NUMBER BETWEEN 1 AND 10 WILL BE SELECTED AT RANDOM.\nYOU WILL TRY TO GUESS THAT NUMBER IN AS LITTLE TRIES AS POSSIBLE.\n')
    high_score = 0
    while True:
        if high_score == False:
            print('NO HIGH SCORE HAS BEEN SET.\n')
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
                    ticker+=1
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
                    print('YOU GOT IT!\nIT TOOK YOU {} TRIES TO GUESS!\nTHE GAME HAS CONCLUDED.\n'.format(ticker))
                    break
                break
            except ValueError:
                print('OOPS! YOU NEED TO ENTER A NUMBER!')
                ticker += 1
        if high_score == 0 or ticker < high_score:
            high_score = ticker
        replay = input('WOULD YOU LIKE TO PLAY AGAIN??\nENTER Y TO PLAY AGAIN.  >> ')
        if replay == 'Y'.lower():
            continue
        else:
            print('OKAY! SEE YOU NEXT TIME!.')
            break

start_game()
