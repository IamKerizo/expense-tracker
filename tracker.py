# Installment 4
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
if amount1 >= 250:
    print("\tHuge expense.")
elif amount1 > 100:
    print("\tBig expense.")
elif amount1 <= 99:
    print("\tSmall expense.")
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
if amount2 >= 250:
    print("\tHuge expense.")
elif amount2 > 100:
    print("\tBig expense.")
elif amount2 <= 99:
    print("\tSmall expense.")
subtotal += amount2

if amount1 > 100 and amount2 > 100:
    print("\tWARNING: Both expenses are big")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget


print("")
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}: \t${amount1:.2f}")
print(f"\t- {item2}: \t${amount2:.2f}")
print(f"Subtotal: \t\t${subtotal:.2f}")
print(f"Average: \t\t${average:.2f}")
print(f"Tax ({tax_percent}%): \t\t${tax:.2f}")
print(f"Grand total: \t\t${total:.2f}")
if over_budget:
    over_amount = total - budget
    print(f"Over budget by ${over_amount:.2f}!")
elif total > 0.9 * budget:
    left_amount = budget - total
    print(f"Careful: only ${left_amount:.2f} left.")
else:
    left_amount = budget - total
    print(f"Within budget. ${left_amount:.2f} left.")
print("-" * 40)
print("Made by: Mark Francis R. Baguistan | Installment 4")


