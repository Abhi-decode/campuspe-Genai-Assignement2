# Take birth year input from the user and convert it to integer
birth_year = int(input("Enter your birth year: "))

# Take current year input from the user and convert it to integer
current_year = int(input("Enter current year: "))

# Check if the birth year is greater than the current year (invalid case)
if birth_year > current_year:
    print("Birth year cannot be greater than current year.")

# Check if the entered years are positive numbers
elif birth_year <= 0 or current_year <= 0:
    print("Year must be a positive number.")

# If inputs are valid, calculate age
else:
    age = current_year - birth_year  # Age calculation
    print("Your age is:", age)  # Display the age