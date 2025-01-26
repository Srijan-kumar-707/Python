def f(num):
    if (num ==0 or num ==1):
        return 1
    else:
        return num * f(num-1)


print(f(10))