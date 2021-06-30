a = int(input())
b = int(input())

for i in range(1, 101, 1):
    if i % 10 <= 5 and i // 10 > 0:
        i = i + 1
        continue
    print(i)
