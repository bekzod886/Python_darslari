soz = input()
EnUz = {
  "i": "men",
  "you": ["sen", "siz"],
    "hello": "salom"
}
soz = soz.lower()

for i in EnUz.keys():
    if i in soz:
        print(EnUz[i])
        break
else:
    print("Bunday soz yuq")