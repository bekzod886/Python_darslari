def yig(a,b):
    return lambda n: (a+b)**n
y = yig(2,3)
print(y(2))
