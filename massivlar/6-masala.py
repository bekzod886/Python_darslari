a = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    if i == len(a)-1:
        a[i]=0
    else:
        a[i] = a[i+1]
print(a)




