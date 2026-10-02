# Installment 3
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")
subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total


print("")
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}: \t${amount1:.2f}")
print(f"\t- {item2}: \t${amount2:.2f}")
print(f"Subtotal: \t\t${subtotal:.2f}")
print(f"Average: \t\t${average:.2f}")
print(f"Tax ({tax_percent}%): \t\t${tax:.2f}")
print(f"Grand total: \t\t${total:.2f}")
print(f"Over budget? \t\t{over_budget}")
print(f"Left in budget: \t${left:.2f}")
print("-" * 40)
print("Made by: Mark Francis R. Baguistan | Installment 3")


