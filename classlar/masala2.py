class xodim:
    def __init__(self, ismi, maoshi):
        self.ismi = ismi
        self.maoshi = maoshi

    def salom(self):
        return f"Mening ismim {self.ismi} maoshim {self.maoshi}"


xodimlar = []

n = int(input('n= '))

for i in range(n):
    print(f"{i + 1} xodim: ")
    ismi = input('ism: ')
    maoshi = int(input('maoshi: '))
    xodimlar.append(xodim(ismi=ismi, maoshi=maoshi))

for xodim in xodimlar:
    if xodim.maoshi > 1000000:
        print(xodim.ismi)
