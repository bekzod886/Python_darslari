def name(name):
    return lambda n: name*n
y = name('Bekzod ')

print(y(3))