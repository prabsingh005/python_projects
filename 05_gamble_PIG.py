from random import randint

if __name__ == "__main__":

    print("""
    Welcome to PIG game
        
    1. you will get a random num from 1 to 6
    2. each num will get add to your total score
    3. if you get 1 your score will become zero and you will lost
    4. you can choose to end the game after successful score
    """)

    total = 0

    start = input("Type 'start' to start the game: ").lower()

    while start != "start":
        print("Invalid input, enter 'start'")
        start = input("Type 'start' to start the game: ").lower()
        
    try:
        while start == "start":
            num = randint(1, 6)

            if num == 1:
                print(f"You lost, the number is {num}")
                total = 0
                print(f"Your score becomes {total}")
                break

            else:
                print(f"You got {num}")
                total += num
                print(f"Your total is {total}\n")

                if total >= 50:
                    print(f"Congratulations you have scored the highest score that is {total}")
                    break

                while True:

                    cont = input("Would you like to continue (Y/N): ").upper()
                    
                    if cont == "Y":
                        break

                    elif cont == "N":
                        print(f"Your total score is {total}")
                        exit()

                    else:
                        print("Enter a valid option")
                        continue

    except Exception as e:
        print(e)