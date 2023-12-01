print("Welcome to the Dice Roll Game, where two dice are rolled and the higher number is the winner! Today, it will be you vs. our undefeated champion, THE COMPUTER!")

question = input("Would you like to roll the dice? (press enter to continue)").upper()
playerOneScore = 0
playerTwoScore = 0

import random
playerOneScore = random.randint(1, 6)
playerTwoScore = random.randint(1, 6)

print("You got: " + str(playerOneScore))
print("The Computer got: " + str(playerTwoScore))

if (playerOneScore > playerTwoScore):
    print("Congratulations! You beat our champion!")
elif (playerTwoScore > playerOneScore):
    print("As to be expected! Better luck next time, player.")
else:
    print("A draw! Try again!")