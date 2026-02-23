# Take total bill amount from user
total_bill = float(input("Enter total bill amount: "))

# Take number of people from user
number_of_people = int(input("Enter number of people: "))

# Validate number of people
if number_of_people <= 0:
    print("Number of people must be greater than zero.")
else:
    split_amount = total_bill / number_of_people
    print(f"Each person should pay: {split_amount:.2f}")