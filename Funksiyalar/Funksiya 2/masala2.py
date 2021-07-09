x = int(input())


def myfunction(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1
    else:
        return -1


a = myfunction(x)
print(a)
