import re

# Function to find a pattern in a file using regex
def find_pattern_in_file(file_name, pattern):
    try:
        # Open the file and read its content
        with open(file_name, 'r') as file:
            content = file.read()
            
            # Find all occurrences of the pattern
            matches = re.findall(pattern, content)
            return matches
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
# Taking user input for file name and regex pattern
file_name = input("Enter the filename (including extension): ")
pattern = input("Enter the regex pattern to search for: ")
# Calling the function and storing the result
matches = find_pattern_in_file(file_name, pattern)
# Displaying the results
if matches:
    print(f"\nFound {len(matches)} matches:")
    for match in matches:
        print(match)
else:
    print("\nNo matches found.")
# Thanking the user
print("\nThank you for using the regex pattern matching program!")