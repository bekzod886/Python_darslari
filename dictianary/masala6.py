soz = input()
EnUz = {
  "i": "men",
  "you": ["sen", "siz"],
    "hello": "salom"
}
soz = soz.lower()
a = []
for i in EnUz.keys():
    if i in soz:
        a.append(EnUz[i])
        print(a)
        break

else:
    print("Bunday soz yuq")