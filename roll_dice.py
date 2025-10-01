import random

roll = random.randint(1,6)
guess = int(input("Guess the dice roll in a range of 1-6: \n"))
if guess == roll:
    print("Correct! the computer rolled a " + str(roll))
else:
    print("Wrong! The computer rolled a " + str(roll))