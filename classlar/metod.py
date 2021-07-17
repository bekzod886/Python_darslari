class Name:
    def __init__(self,viloyat,tuman,mahalla):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahalla = mahalla


    def adres(self):
        #print(f"{self.viloyat} viloyati {self.tuman} tumani {self.mahalla} mahallasi")
        return self.viloyat + ' ' + self.tuman + ' '+ self.mahalla

sh1 = Name('Jizax','Baxmal','Bog\'ishamol')
print(sh1.adres())

