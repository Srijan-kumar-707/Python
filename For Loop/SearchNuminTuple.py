tup = (1,2,4,16,25,36,49,64,81,100)
n = int(input("Enter a number: "))
flag = False
idx = 0
for i in tup:
    if (n == i):
        flag = True
        break
    idx += 1

if (flag == True):
    print("Found at index : ",idx)
else:
    print("Not found")
