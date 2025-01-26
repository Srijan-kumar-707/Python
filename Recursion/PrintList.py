def printList(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    printList(list, idx+1)

l= [1,2,3,4,5,45,18,100,34]
printList(l)