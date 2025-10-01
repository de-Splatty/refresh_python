import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("rock, paper or scissors, what is your choice? \n")

print("The computer chose: " + computer_choice)

if user_choice == computer_choice:
    print("both players tied!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you win!")
else:
    print("you lose!")