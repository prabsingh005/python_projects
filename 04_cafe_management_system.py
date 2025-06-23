opt = {"pizza": 40,
       "pasta": 50,
       "burger": 60,
       "salad": 70,
       "coffee": 80
       }

print(
    "Pizza: Rs40\n"
    "Pasta: Rs50\n"
    "Burger: Rs60\n"
    "Salad: Rs70\n"
    "Coffee: Rs80"
    )

order = []

try:
    while True:

        items = input("Enter the items your want to order: ").lower()

        if items in opt:
            print(f"{items} has been added")
            order.append(items)

        else:
            print("Enter a valid option")

        cont = input("do you want to add more (yes/no): ").lower()
            
        if cont == "yes":
            continue

        else:
            # total = sum(opt[items] for items in order)

            total = 0

            for items in order:
                if items in opt:
                    total += order[items]

            print(f"Your total is {total}")
            break

except Exception as e:
    print(e)