import os

def get_filename(prompt, default):
    name = input(f"{prompt} (default: {default}): ").strip()
    return name if name else default

# 1. Writing to a File
def write_to_file():
    filename = get_filename("Enter filename to write to", "sample.txt")
    content = input("Enter content to write to the file: ")
    with open(filename, 'w') as file:
        file.write(content + "\n")
    print(f"Written to {filename}.")

# 2. Reading from a File
def read_file():
    filename = get_filename("Enter filename to read from", "sample.txt")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print("File contents:\n", content)
    else:
        print("File does not exist.")

# 3. Appending Data to a File
def append_to_file():
    filename = get_filename("Enter filename to append to", "sample.txt")
    content = input("Enter content to append: ")
    with open(filename, 'a') as file:
        file.write(content + "\n")
    print("Data appended.")

# 4. Reading a File Line by Line
def read_line_by_line():
    filename = get_filename("Enter filename to read line-by-line", "sample.txt")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print("Reading line by line:")
            for line in file:
                print(line.strip())
    else:
        print("File does not exist.")

# 5. Counting Words in a File
def count_words():
    filename = get_filename("Enter filename to count words in", "sample.txt")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            words = file.read().split()
        print("Word count:", len(words))
    else:
        print("File does not exist.")

# 6. Copying File Content
def copy_content():
    source = get_filename("Enter source filename", "sample.txt")
    dest = get_filename("Enter destination filename", "copy.txt")
    if os.path.exists(source):
        with open(source, 'r') as src, open(dest, 'w') as dst:
            dst.write(src.read())
        print(f"Copied content to {dest}.")
    else:
        print("Source file does not exist.")

# 7. Checking if a File Exists
def check_file_exists():
    filename = get_filename("Enter filename to check", "sample.txt")
    exists = os.path.exists(filename)
    print(f"File exists: {exists}")
    return exists

# 8. Writing a List to a File
def write_list_to_file():
    filename = get_filename("Enter filename to write list into", "sample.txt")
    data = input("Enter list items separated by commas: ").split(',')
    with open(filename, 'w') as file:
        for item in data:
            file.write(item.strip() + "\n")
    print("List written to file.")

# Menu to run functions
def menu():
    print("""
1. Write to file
2. Read file
3. Append to file
4. Read line by line
5. Count words
6. Copy content to another file
7. Check file exists
8. Write list to file
9. Exit
    """)

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            write_to_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            append_to_file()
        elif choice == '4':
            read_line_by_line()
        elif choice == '5':
            count_words()
        elif choice == '6':
            copy_content()
        elif choice == '7':
            check_file_exists()
        elif choice == '8':
            write_list_to_file()
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()