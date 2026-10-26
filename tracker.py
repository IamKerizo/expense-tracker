# Installment 5
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

subtotal = 0
count = 0
choice = ""

while choice != "4":

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        if amount > 200:
            print("\tHuge expense - are you sure?")
        elif amount > 100:
            print("\tBig expense.")
        elif amount > 50:
            print("\tModerate expense.")
        else:
            print("\tSmall expense.")
        subtotal += amount
        count += 1

    elif choice == "2":
        print("\tComing soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        print(f"\tExpenses:\t\t{count}")
        print(f"\tSubtotal: \t\t${subtotal:.2f}")
        print(f"\tTax ({tax_percent}%): \t\t${tax:.2f}")
        print(f"\tGrand total: \t\t${total:.2f}")

        over_budget = total > budget

        if over_budget:
            over_amount = total - budget
            print(f"\tOver budget by ${over_amount:.2f}!")
        elif total > 0.9 * budget:
            left_amount = budget - total
            print(f"\tCareful: only ${left_amount:.2f} left.")
        else:
            left_amount = budget - total
            print(f"\tWithin budget. ${left_amount:.2f} left.")

    elif choice == "4":
            print(f"Goodbye, {name}!")
            
    else:
            print("Please choose 1, 2, 3 or 4.")

print("-" * 40)
print(f"Made by: Mark Francis R. Baguistan | Installment 5")
print("=" * 40)


