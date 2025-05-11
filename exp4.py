# Program to sort a list using a simple sorting algorithm and an in-built function

# Taking user input for the list size
n = int(input("Enter the number of elements required: "))
# Creating an empty list
l2 = []
# Taking list elements from the user
print("Enter the elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    l2.append(element)
# Displaying the original list
print("\nOriginal List:", l2)
# Sorting using a simple sorting algorithm (Bubble Sort)
for i in range(len(l2)):
    for j in range(i + 1, len(l2)):
        if l2[i] > l2[j]:
            # Swapping elements
            l2[i], l2[j] = l2[j], l2[i]
# Displaying the sorted list
print("Sorted List (using custom algorithm):", l2)
# --- Sorting using an in-built function ---
# Taking input again for comparison
l1 = []
print("\nUsing in-built sort function:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    l1.append(element)
# Displaying the original list
print("\nOriginal List:", l1)
# Sorting using Python's built-in `sort()` function
l1.sort()
# Displaying the sorted list
print("Sorted List (using in-built sort):", l1)
# Thanking the user
print("\nThank you for using the sorting program!")