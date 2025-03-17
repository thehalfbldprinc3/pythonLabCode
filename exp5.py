#Simple reverse
def reverseString(string):
    reverseStr = ""

    for i in range(len(string)-1, -1, -1):
        reverseStr+= string[i]
    
    return reverseStr

# Reverse using library function
def reverseString2(string):
    string="".join(reversed(string))
    
    return string

string = input("enter the string: ")
reverseStr= reverseString(string)
reverseStr2= reverseString2(string)

print("Original String: ", string)
print("Reversed String: ", reverseStr)
print("Reversed String using Library Function: ", reverseStr2) 