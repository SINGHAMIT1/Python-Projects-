# Multiple Inputs with Python using While Loop
# The "while true" loop in python runs without any conditions
# until the break statement executes inside the loop.
while True:
    reply = input("Write your message :").lower()
    if reply == "stop":
        break
    print(reply)
