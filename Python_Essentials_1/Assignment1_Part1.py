# Take user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age_input = input("Enter your age: ")

# Check if age is numeric
if not dage_input.isdigit():
    print("Invalid age input")
else:
    age = int(age_input)

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative")
    else:
        # Print full name using string concatenation
        full_name = first_name + " " + last_name
        print("Full Name: " + full_name)

        # Print age next year
        print("You will be " + str(age + 1) + " next year")
