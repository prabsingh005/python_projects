from random import choice

opt = ["R", "P", "S"]
count = 0

print("Best of three rock, paper and scissors game\n")

for i in range(1,4):

    computer = choice(opt)
    option = input("Choose one r = 'rock', p = 'paper', s = 'scissor'): ").upper()

    if computer == option:
        print("It's a draw")

    elif computer == "R" and option == "P" or \
         computer == "P" and option == "S" or \
         computer == "S" and option == "R":
        
        count += 1

        print("you won")

    else:
        print("you lost, try again")

print(f"you won {count} times")