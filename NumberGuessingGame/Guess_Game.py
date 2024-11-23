import random

top_of_range = input("Type a number: ")

#Make sure user type a number greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time!")
        quit()
else:
    print("Please type a number next time!")
    quit()
    
random_number = random.randint(0, top_of_range)

#This to keep track of how many guesses the user make
guesses = 0

#Exit once the user type the correct number
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    #Tell the user if they guessed above or below the number
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

#once the game finish print this
print("You got it in", guesses, "guesses!")


#Notes:
#random.randrange(start,stop) but doesn't include the stop
#random.randrange(stop) just with stop this will generate random number starting from zero

#random.randint(start,stop) this will include the stop number

#When taking input from the user, for example they type 25 this is red as a string "25" so we will convert it to int, and make sure it is
# digit because if they type "Hello" this produce an error