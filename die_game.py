import random

def roll_die():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total
def main():
 player1 = input("Enter name for Player 1: \n")
 player2 = input("Enter name for Player 2: \n")

 roll1 = roll_die()
 roll2 = roll_die()

 print(player1, "rolled:", roll1)
 print(player2, "rolled:", roll2)

 if roll1 > roll2:
    print(player1, "wins!")
 elif roll2 > roll1:
    print(player2, "wins!") 
 else:
    print("It's a tie!")
    
main()