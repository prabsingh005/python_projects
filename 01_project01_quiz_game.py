# Quiz game

print("You have entered a quiz game!")

correct = 0

print('''Q1. What is the capital of Australia?
    A. Sydney
    B. Melbourne
    C. Perth
    D. Canberra
''')
op1 = input("Enter the option: ").upper()
if op1 == "D":
    correct += 1

print('''
Q2. Which planet is known as the Red Planet?
    A. Earth
    B. Venus
    C. Mars
    D. Jupiter
''')
op2 = input("Enter the option: ").upper()
if op2 == "C":
    correct += 1

print('''
Q3. Who invented the light bulb?
    A. Alexander Graham Bell
    B. Thomas Edison
    C. Isaac Newton
    D. Nikola Tesla
''')
op3 = input("Enter the option: ").upper()
if op3 == "B":
    correct += 1

print('''
Q4. What is the chemical symbol for Gold?
    A. Ag
    B. Gd
    C. Au
    D. Go
''')
op4 = input("Enter the option: ").upper()
if op4 == "C":
    correct += 1

print('''
Q5. Which is the longest river in the world?
    A. Amazon River
    B. Mississippi River
    C. Yangtze River
    D. Nile River
''')
op5 = input("Enter the option: ").upper()
if op5 == "D":
    correct += 1

print(f"Your score is {correct} out of five")

if correct == 5:
    print("Excellent! You're a quiz master!")

elif correct >= 3:
    print("Good job! Keep learning.")

else:
    print("Better luck next time! Try again.")