import random

def guess_the_number():
    return random.randint(1, 100)

def main():
    number = guess_the_number()
    print("I'm thinking of a number between 1 and 100.")
    while True:
        guess = int(input("What's your guess? "))

        if guess < number / 2:
            print("A lot higher!")
        elif guess < number:
            print("Higher!")
        elif guess > number * 2:
            print("A lot lower!")
        elif guess > number:
            print("Lower!")
        else:
            print("You got it!")

main()