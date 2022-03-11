#5)Write a program to sort list of strings (similar to that of dictionary)
a=[]
n=int(input("enter size of the list:"))
for i in range(n):
    val=input("enter strings in a list:")
    a.append(val)



print("\nList of strings Before sorting:")
print(a)
# sorting the list in ascending order
a.sort()
# printing the sorted list
print("\nList of strings after sorting:")
print(a)
