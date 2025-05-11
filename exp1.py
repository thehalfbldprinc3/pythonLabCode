# Program to prompt the user for their name and age, then display a personalized message

# Taking user input for name and age
name = input("Enter your name: ")  # Accepts a string input for the name
age = input("Enter your age: ")    # Accepts a string input for the age

# Type conversion: Convert age from string to integer
try:
    age = int(age)
except ValueError:
    print("Invalid age! Please enter a numeric value.")
    exit()

# Processing and output
# Displaying a personalized message using string formatting
print(f"Hello, {name}! You are {age} years old.")

# Simple operation: Calculate the age in 5 years
future_age = age + 5
print(f"In 5 years, you will be {future_age} years old.")

# Thanking the user
print("Thank you for using this program!")