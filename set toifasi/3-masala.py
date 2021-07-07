import random

meva = []
for i in range(0,10):
    meva.append(random.randint(1,10))
meva = set(meva)
print(meva)