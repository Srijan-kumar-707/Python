#WAP to store 3 things in a list......
m1 = input("Enter first movie: ")
m2 = input("Enter second movie: ")
m3 = input("Enter third movie: ")
list = []
list.append(m1)
list.append(m2)
list.append(m3)
print(list)

#Check palindrome....
list = [1,2,3,2,1]
list1 = list.copy()
list1.reverse()
if (list == list1):
    print("Palindrome")
else:
    print("Not Palindrome")