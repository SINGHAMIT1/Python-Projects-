import random

# taking input from user
passlen = int(input("enter the length of the password you want to generate :"))
# declaring a string of numbers + uppercase + lowercase + special characters
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?."
# sample() returns a particular length list of items chosen from the sequence
password = "".join(random.sample(s, passlen))
print(password)
