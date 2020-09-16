from numpy import random
import sys





def guessingGame(range,highscore,currentPlayerScore,attempts):
    highScore=highscore
    currentPLayerScore=0
    attempts=0
    range=range
    
    print("Welcome to the guessing game\n")
    print(f'The highest score is {highScore} goodluck\n')

    randomNum= random.randint(int(range))

    guess = -1


    while guess != randomNum :
        guess=input("Please choose a number\n:")
        if attempts > 10:
            print("Sorry you lose maximum attempts \n ")
            choice = input("would you like to play again? y or n\n")
            if choice == 'y':
                return guessingGame(3,highScore,0,0)
            else:
                return print("Thanks for playing Bye :)\n")
                sys.exit()
        elif int(guess) > randomNum:
            print("It is less than that\n")
            attempts+=1
        elif int(guess) < randomNum:
            print("It is more than that\n")
            attempts+=1
        
        else:
            currentPLayerScore = 10 - attempts
            if currentPLayerScore > highScore:
                highScore = currentPLayerScore
                print(f"You won and you have the new highest score of {highScore}")
                choice = input("would you like to play again? y or n\n")
                if choice == 'y':
                    return guessingGame(3,highScore,0,0)
                else:
                    return print("Thanks for playing Bye :)\n")
                    sys.exit()
            else:
                print("you won!")
                choice = input("would you like to play again? y or n\n")
                if choice == 'y':
                    return guessingGame(3,highScore,0,0)
                else:
                    return print("Thanks for playing Bye :)\n")
                    sys.exit()
        
    
guessingGame(3,0,0,0)
        
            

        
    



