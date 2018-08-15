import random
number = random.randint(1,5)
Guesses = 0
win = False 

name = input("Welcome to Amirah's Game")
name = input("Enter your name")

print("Hello  " + name + "." )

question = input("Are you ready ? [Y/N] ")


if question.lower() == "n": 
    print(":(")
    exit()


if question.lower() == "n": 
    print(":(")
    exit()
if question.lower() == "y":
    print("I'm thinking of a number between 1 and 5")
while not win: 
    guess = int(input("Guess the number ..."))
    Guesses = Guesses + 1
    if guess == number:
        win = True 
    elif guess < number:
      print("Umm " +"Guess Higher" )

    elif guess > number:
        print("Umm " +"Guess Lower")
print("Great you won! The number was {}".format(number))
print("you had taken {} guesses to win".format(Guesses))