import os

# Displaying the list of files before copying
print("List of files before copying:")
print(os.listdir())
print("\n")
# Opening file1.txt in read mode
with open('file1.txt', 'r') as file1:
    # Opening file2.txt in write mode
    with open('file2.txt', 'w') as file2:
        # Copying content line by line
        for line in file1:
            file2.write(line)
# Reading and displaying the contents of file2.txt
with open('file2.txt', 'r') as file2:
    print("Contents of file2.txt:\n")
    print(file2.read())
# Displaying the list of files after copying
print("\nList of files after copying:")
print(os.listdir())
print("\n")
# Thanking the user
print("Thank you for using the file handling program!")