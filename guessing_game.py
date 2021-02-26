"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random



def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # Display welcome message to user
    print('------------------------------------------------------------')
    print('            WELCOME TO THE NUMBER GUESSING GAME             ')
    print('------------------------------------------------------------')
    print('IN THIS GAME, A NUMBER IN A RANGE WILL BE SELECTED AT RANDOM.\nYOU WILL TRY TO GUESS THAT NUMBER IN AS LITTLE TRIES AS POSSIBLE.\n')
    while True:
        print('TO BEGIN, PLEASE SELECT A DIFFICULTY... EASY, MEDIUM, HARD?')
        print('EASY: 1-10')
        print('MEDIUM: 1-25')
        print('HARD: 1-50')
        difficulty = input('>>   ')

        if difficulty == 'easy'.lower():
            num = random.randrange(10)
            print('THE NUMBER IS BETWEEN 1-10...')
        elif difficulty == 'medium'.lower():
            num = random.randrange(25)
            print('THE NUMBER IS BETWEEN 1-25...')
        else:
            num = random.randrange(50)
            print('THE NUMBER IS BETWEEN 1-50..')

        ticker = 1
        while True:
            guess = int(input('ENTER A NUMBER >>   '))
            try:
                if guess < num:
                    print('THE NUMBER IS HIGHER...')
                    ticker += 1
                    continue
                if guess > num:
                    print('THE NUMBER IS LOWER...')
                    ticker += 1
                    continue
                if guess == num:
                    print('YOU GOT IT! GREAT JOB!\nIT ONLY TOOK YOU {} TRIES!'.format(ticker))
                    break
            except ValueError:
                print('OOPS! YOU NEED TO ENTER A NUMBER!')
        replay = input('WOULD YOU LIKE TO PLAY AGAIN?? Y/N   ')
        if replay == 'y'.lower():
            continue
        else:
            print('OKAY! GOODBYE.')






# Kick off the program by calling the start_game function.
start_game()
