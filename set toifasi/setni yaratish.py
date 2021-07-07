"""numbers = {1, 2, 3, 4, 5, 2, 5, 2}
i = 0
a=[]
#print(numbers)
#print(len(numbers))
for number in numbers:
    #print(number)
    i+=1
    if i%2==1:
        a.append(number)
print(a)"""
harf1 = {"a", "b", "c", "d"}
harf2 = {"c", "e", "e", "f"}
harf3 = harf1.union(harf2)
print(harf3)
meva = {"nok", "banan", "shaftoli"}
x = meva.pop()
print(x)
print(meva)

