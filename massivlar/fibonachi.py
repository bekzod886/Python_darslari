son = int(input())
count = 0
a = []
n1 = 0
n2 = 1
while count < son+1:
       a.append(n2)
       yig = n1 + n2
       n1 = n2
       n2 = yig
       count += 1

print(a)


