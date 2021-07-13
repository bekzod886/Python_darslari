def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    else:
        for i in range(1, n+1):
            c = a + b
            #1,2,3,5,8,13
            print(c)
            a = b
            b = c
        return b
print(fibonacci(9))