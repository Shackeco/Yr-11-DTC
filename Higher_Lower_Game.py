import random

guesses = 10
number = (random.randint(1, 100))
guess = None
print(f"The computer has generated a number, you have {guesses} guesses")
while guess != number:
    valid = False
    while not valid:
        guess = input(f"Enter a whole number between 1 and 100. \n")
        try: 
            guess = int(guess)

            if guess < 1 or guess > 100:
                print("That is invalid, Retry")
            else:
                valid = True
        except ValueError:
                print("That is invalid, Retry")

    if guess < number:
        print("That number is too low")
    if guess > number:
        print("That number is too high")
    if guess == number:
        print(f"Good job my guy! You got it right! \n You had {guesses} guesses left")
        break
    if guesses <= 1:
        print("Oh no, you got rekt, no more guesses for you")
        break
    guesses -= 1
    print(f"you have {guesses} guesses left")