number= int(input("Enter a number: "))
fact=1
if(number<0):
    print("Factorial of negative number Does not exist")
elif(number==0):
    print("Factorial of 0 is 1")
else:
    for i in range(1, number+1):
        fact= fact*i