# Program to check if a user is eligible to vote

# Taking user input for age
age = input("Enter your age: ")

# Type conversion and validation
try:
    age = int(age)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit()

# Checking voting eligibility
if age >= 18:
    print("You are eligible to vote in the next election.")
else:
    print("You are not eligible to vote yet.")

# Thanking the user
print("Thank you for using the voting eligibility checker!")