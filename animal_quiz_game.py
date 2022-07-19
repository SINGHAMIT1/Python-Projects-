""" Quiz Game with Python
1. at first, I will create the questions and answers verification mechanism
2. give the player three attempts to answer each question"""


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Your answer is correct! ")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("wrong answer, try again")
        attempt += 1
    if attempt == 3:
        print("The correct answer is", answer)


score = 0
print("Guess the animal ")
guess1 = input("What is the mascot of IUPUI ?")
check_guess(guess1, "JAGUAR")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "Blue Whale")
print("Your score is :" + str(score))
