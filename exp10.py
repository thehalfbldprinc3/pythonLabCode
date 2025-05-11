# Function to divide two numbers with exception handling
def divide_numbers():
    try:
        # Taking user input for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))  
        # Performing division
        result = num1 / num2 
        # Displaying the result
        print(f"\nThe result of {num1} divided by {num2} is: {result:.2f}")
    # Handling invalid numeric input
    except ValueError:
        print("\nError: Please enter valid numeric values.") 
    # Handling division by zero
    except ZeroDivisionError:
        print("\nError: Division by zero is not allowed.")
    # Handling other unexpected errors
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
# Calling the function
divide_numbers()