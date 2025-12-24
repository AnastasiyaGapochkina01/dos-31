import random

guess = 23
#random.randint(1,100)

print(f"Hello! Let`s play!")
user_input = input("Enter number: ")

if user_input.isdigit():
   user_input = int(user_input)
   if user_input == guess:
     print("Great! You win")
   elif guess < user_input:
     print("Guess number few than yours")
   else:
    print("Guess number great than yours")
else:
    print("Incorrect input")


#print(f"User input = {user_input}; type: {type(user_input)}")