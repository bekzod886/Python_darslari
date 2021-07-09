a = int(input("a: "))
b = int(input("b: "))


def max(a, b):
    if a > b:
        return a
    else:
        return b


d = max(a, b)
print(d)
