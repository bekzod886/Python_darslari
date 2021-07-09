soz = input()
soz = soz.split(" ")
enUz = {
  "i": "men",
  "world": "dunyo",
    "hello": "salom"
}
a = []
print(soz)
for i in enUz.keys():
    for j in soz:
        if i == j:
            a.append(enUz[i])

        break
print(a)