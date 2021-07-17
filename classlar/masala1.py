class xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi

    def maosh(self):
        print(f"Mening ismim {self.ismi} maoshim {self.maoshi}")


sh1 = xodim('Bekzod', 'Jizzax', 120000)
sh2 = xodim('Davron', 'Jizzax', 2000000)
sh3 = xodim('Ali', 'Jizzax', 2300000)
sh4 = xodim('Hasan', 'Jizzax', 12000000)
sh5 = xodim('Jamshid', 'Jizzax', 1200000)

xodimlar = []
xodimlar.append(sh1)
xodimlar.append(sh2)
xodimlar.append(sh3)
xodimlar.append(sh4)
xodimlar.append(sh5)

for i in xodimlar:
    i.maosh()
