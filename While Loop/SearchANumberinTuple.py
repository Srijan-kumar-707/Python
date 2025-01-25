tup = (1,2,3,4,5)
n = int(input("Enter a number : "))
i = 0
flag = True
while i < len(tup):
    if (n == tup[i]):
        flag = False
    i = i + 1

if (flag == False):
    print("Found")
else:
    print("Not Found")