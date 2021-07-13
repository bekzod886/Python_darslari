import math

n = int(input("n soni: "))


def factor(n):
    if n == 1:
        return 1
    else:
        return n + factor(n - 1)


print(factor(n))
