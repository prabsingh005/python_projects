from random import choice

print("Welcome to the lucky slot machine")
print("----------------------------------\n")
print("Betting amount on each line is Rs.10")
balance = 500
print(f"Current balance: Rs.{balance}")

characters = ['A', 'B', 'C']
win = 0
lose = 0

try:
    while True:
        
        bets = int(input("How many lines do you want to bet on (1-3): "))
        total_bets = 10 * bets

        for i in range(bets):
            slot1 = choice(characters)
            slot2 = choice(characters)
            slot3 = choice(characters)
            print(f"{slot1} | {slot2} | {slot3}")

            balance -= (bets * 10)
            if balance <= 0:
                print(f"Your balance left is {balance}")
                exit()

            if slot1 == slot2 == slot3:
                print(f"You won Rs.20")
                win += 20

            else:
                print("You won Rs.0")

        while True:    
            cont = input("Do you want to continue betting (Y/N): ").lower()

            if cont == "y":
                break

            else:
                print(f"Your remaining balance is Rs.{balance}")
                exit()

except Exception as e:
    print(e)