import random
def main():
    guess = int(input("What is your guess?"))
    number = random.randint(1, 100)
    game(guess, number)
def game(guess, number):
    while guess != number:
        guess = int(input("Guess again!"))
        if guess > number:
            print("Lower!")
        elif guess < number:
            print("Higher!")
    else:
        print("Congratulation you guessed the number!")

main()