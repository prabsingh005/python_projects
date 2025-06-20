from random import randint

num = randint(1,100)
tries = 1

while True:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess > 100 or guess < 1:
        print("Enter a valid number between 1 and 100")
        continue

    if guess == num:
        print(f"You guessed the number in {tries} tries")
        break

    if guess > num:
        print("Guess lower, try again")

    elif guess < num:
        print("Guess higher, try again")

    tries += 1