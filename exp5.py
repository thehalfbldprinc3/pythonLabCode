# Program to reverse a string using a loop and a library function

# Function to reverse a string using a loop
def reverseString(string):
    reverseStr = ""
    for i in range(len(string) - 1, -1, -1):
        reverseStr += string[i]
    return reverseStr

# Function to reverse a string using a library function
def reverseString2(string):
    return "".join(reversed(string))

# Taking user input
string = input("Enter the string: ")

# Calling both functions
reverseStr = reverseString(string)
reverseStr2 = reverseString2(string)

# Displaying results
print("\nOriginal String:", string)
print("Reversed String (using loop):", reverseStr)
print("Reversed String (using library function):", reverseStr2)

# Thanking the user
print("\nThank you for using the string reversal program!")