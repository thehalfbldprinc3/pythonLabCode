import os

print("List of files before: ")
print(os.listdir())
print("\n")


file1= open('file1.txt', 'r')

file2= open('file2.txt', 'w')

for line in file1:
    file2.write(line)


file1.close()
file2.close()


file2= open('file2.txt', 'r')


print(file2.read())


file2.close


print('\n')
print("List of files after: ")
print(os.listdir())
print('\n')