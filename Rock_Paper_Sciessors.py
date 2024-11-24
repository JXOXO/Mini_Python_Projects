import random

#To track the winner
user_wins = 0
computer_wins = 0

#list of possible values
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock / Paper / Scissors / Q to quite the game: ").lower() #make any input lowercase
    if user_input == "q":
        break
    
    #User input is valid choice if not ask user again until they input valid play
    if user_input not in options:
        continue
    
    # Rock: 0, Paper: 1, Scissor: 2, Computer make a random choice
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    #winning conditions
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    #User lost
    else:
        print("You lost!")
        computer_wins += 1

#Results
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")

if user_wins > computer_wins:
    print("You won against the computer. GoodJob!")
elif computer_wins > user_wins:
    print("Computer got more wins. GoodLuck next time!")
else:
    print("It is a tie. GoodLuck next time!")