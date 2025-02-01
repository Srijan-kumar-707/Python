import numpy as np

l = [1,2,3,4,5]
print(l)

#Using numpy we can create multidimensional Array......
a = np.array([1,2,3,4,5])
print(a)

print("3d Array: ")
arr = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(arr)

print(type(a))
print(type(arr))
print(len(l))
print(a.size)
print(arr.size)

#shape gives the rows and column
print(a.shape)
print(arr.shape)


