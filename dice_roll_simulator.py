import random
min_value=1
max_value=6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "Yes" or roll_again == "YES":
    print("Rolling the dices.......")
    print("The values are :")
    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))
    roll_again = input("do you want to roll again? ")
