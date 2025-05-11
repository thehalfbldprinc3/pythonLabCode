# Program to calculate the factorial of a number using a loop

# Taking user input
num = input("Enter a number to calculate its factorial: ")

# Type conversion and validation
try:
    num = int(num)
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        exit()
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit()

# Initializing factorial to 1
factorial = 1

# Calculating factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Displaying the result
print(f"The factorial of {num} is {factorial}.")

# Thanking the user
print("Thank you for using the factorial calculator!")