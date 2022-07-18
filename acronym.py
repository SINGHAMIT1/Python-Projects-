# taking an input from user
user_input = str(input("Enter a prompt : "))
# splitting the prompt into word
word = user_input.split()
# taking an empty string to store the acronym
acr = ""
# looping
for i in word:
    acr = acr + str(i[0].upper())
print(acr)
