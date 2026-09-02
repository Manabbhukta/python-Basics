import random

print(" Number Guessing Game ")
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1-100: "))

    if guess == secret_number:
        print(" Correct! You Won!")
        break
    elif guess < secret_number:
        print("Try a bigger number")
    else:
        print("Try a smaller number")
