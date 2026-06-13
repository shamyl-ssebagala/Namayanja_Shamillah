
# This program calculates how much each person should pay including tip

# GET INPUTS FROM USER 

# Get total bill amount
total_bill = float(input("Enter the total bill amount: $"))

# Get number of people
num_people = int(input("Enter the number of people: "))

# Get tip percentage
print("\nTip options: 10%, 15%, 20%")
tip_choice = input("Choose tip percentage (10/15/20) or enter custom amount: ")

# tip percentage based on user input
if tip_choice == "10":
    tip_percent = 10
elif tip_choice == "15":
    tip_percent = 15
elif tip_choice == "20":
    tip_percent = 20
else:
    # Custom tip amount
    tip_percent = float(tip_choice)

# Calculate tip amount
tip_amount = total_bill * (tip_percent / 100)

# Calculate total bill with tip
total_with_tip = total_bill + tip_amount

# Calculate amount per person
amount_per_person = total_with_tip / num_people

#THE RECEIPT 
print("\n" + "=" * 35)
print("         RECEIPT")
print("=" * 35)

# Using f-strings 
print(f"Subtotal:       ${total_bill:.2f}")
print(f"Tip ({tip_percent}%):        ${tip_amount:.2f}")
print(f"Total:          ${total_with_tip:.2f}")
print(f"Split between:  {num_people} people")
print("-" * 35)
print(f"Each person pays: ${amount_per_person:.2f}")
print("=" * 35)

print("\nThank you! Have a great day!")