import re
def findPatternInFile(file1, pattern):
    try:
        with open(file1, 'r') as file:
            text= file.read
            
            matches = re.findall(pattern, text)
            return matches
    except FileNotFoundError:
        print(f"Error: The file '{file1}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

file1 = input("Enter the filename (including extension): ")
pattern = input("Enter the regex pattern to search for: ")

matches = findPatternInFile(file1, pattern)
if matches:
    print(f"Found {len(matches)} matches:")
    for match in matches:
        print(match)
else:
    print("No matches found.")