from numpy import random
import sys


def converToInt(num):
    try:
        number=int(num)
        return number
    except ValueError:
         return False

def checkNum(num,rand):
    if int(num)== int(rand):
        return "correct"
    elif int(num)> int(rand):
        return  "more"
    else:
        return "less"


def guessingGame(scope,highscore,attempts,cur):
    if int(highscore) < 10:
        highScore=highscore
    else:
        highScore=10
    attempts=attempts
    scope=scope
    
    if attempts==0:
        print("Welcome to the guessing game\n")
        print(f'The highest score is {highScore} goodluck\n')
 
    if int(cur)==100:
        
        randomNum= random.randint(1,10)

    else:
        
        randomNum=int(cur)

    guess = "start"


    if attempts > 10:
        print("Sorry you lose maximum attempts \n ")
        choice = input("would you like to play again? y or n\n")
        if choice == 'y':
            return guessingGame(3,highScore,0,100)
        else:
            return print("Thanks for playing Bye :)\n")
            sys.exit()
    
    while converToInt(guess) == False:
        guess =input("Please enter an integer\n")
       
          

    if checkNum(int(guess),randomNum)=="more":
        print(randomNum)
        print("its less than that")
        attempts+=1
        return guessingGame(3,highScore,attempts,randomNum)
    elif checkNum(int(guess),randomNum)=="less":
        print(randomNum)
        print("its more than that")
        
        attempts+=1
        return guessingGame(3,highScore,attempts,randomNum)
    
            
    elif checkNum(int(guess),randomNum)=="correct":
        if attempts < highScore:
            highScore = attempts
            print(f"You won and you have the new highest score of {attempts} attempts")
            choice = input("would you like to play again? y or n\n")
            if choice == 'y':
                return guessingGame(3,highScore,0,100)
            else:
                return print("Thanks for playing Bye :)\n")
                sys.exit()
        else:
            print(f"you won! with {attempts} attempts \n")
                    
            choice = input("would you like to play again? y or n\n")
            if choice == 'y':
                print(f'The highest score is {highScore} goodluck\n')
                return guessingGame(3,highScore,attempts,100)
            else:
                return print("Thanks for playing Bye :)\n")
                sys.exit()
            
    
guessingGame(3,0,0,100)
        
            

        
    



