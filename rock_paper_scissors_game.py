import random

# choices = ["Rock", "Paper", "Scissors"]
# computer = random.choice(choices)
player = False
player_score = 0
com_score = 0

while True:
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    player = input("Rock, Paper, or Scissors ?").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
            com_score += 1
        else:
            print("You Win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Rock":
            print("You Win!", player, "covers", computer)
            player_score += 1
        else:
            print("You Lose!", computer, "cuts", player)
            com_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            com_score += 1
        else:
            print("You Win!", player, "cuts", computer)
            player_score += 1

    elif player == "End":
        print("Player Total  Score :", player_score)
        print("Computer Total Score :", com_score)
        # comparing total scores to get the final result
        if player_score == com_score:
            print("Final Result TIE")
        elif player_score > com_score:
            print("Player Wins")
        else:
            print("Computer Wins")
        break
        # ending the program
