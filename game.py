computer_choice = "rock"
user_choice = input("rock, paper or scissors, what do you choose? \n")

if user_choice == computer_choice:
    print("Oh, that's a tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Winner, winner, chicken dinner!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Winner, winner, chicken dinner!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Winner, winner, chicken dinner!")
else:
    print("You lose, mate!")
    