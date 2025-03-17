#Simple Sort
l2 = []
n = int(input("Enter the number of elements required: "))
for i in range(0,n):
    element = int(input())
    l2.append(element)

print("Original List: ", l2)

for i in range(0, len(l2)):
    for j in range(i+1, len(l2)):
        if l2[i]>=l2[j]:
            temp=l2[i]
            l2[i]=l2[j]
            l2[j]=temp


print("Sorted List:", l2)

#Sort using in-built function
# l1 = []
# n = int(input("Enter the number of elements required: "))
# for i in range(0,n):
#     element = int(input())
#     l1.append(element)

# print("Original List: ", l1)

# l1.sort()

# print("Sorted List:", l1)