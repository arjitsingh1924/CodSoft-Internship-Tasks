# RockPaperScissors
import random
list = ["Rock","Paper","Scissors"]
print("Hello Buddy, Let's play RockPaperScissors! ")
print("Let's begin......")
userguess = input(("Guess one out of [Rock,Paper,Scissors]: "))

def rockPaperScissors(userguess):
    computerguess = random.choice(list)
    print(f"Computer's guess: {computerguess}")
    
    if (userguess == computerguess):
        print("It's tie !")
        
    elif  userguess == "Rock" and computerguess == "Paper":
        print("You won !")
    elif userguess == "Scissors" and computerguess =="Paper":
        print("You won !")
    elif userguess == "Rock" and computerguess == "Scissors":
        print("You won !")
    else:
        print("computer won. Best of Luck try again next time !")
rockPaperScissors(userguess)        
