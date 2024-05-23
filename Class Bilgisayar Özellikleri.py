class Bilgisayar():
    def __init__(self,name,ram,ssd,islemci,ekran_karti,hz):
        self.name = name
        self.ram = ram
        self.ssd = ssd
        self.islemci = islemci
        self.ekran_karti = ekran_karti
        self.hz = hz
   
    
bilgisayar = Bilgisayar("DELL",16,512,"i5 12500H","RTX 3050",120)
print(bilgisayar)


class Bilgisayar():
    def __init__(self,name,ram,ssd,islemci,ekran_karti,hz):
        self.name = name
        self.ram = ram
        self.ssd = ssd
        self.islemci = islemci
        self.ekran_karti = ekran_karti
        self.hz = hz

    def __str__(self):
        return "Isim : {}\nRam : {}\nSSD : {}\nIslemci : {}\nEkran Karti : {}\nEkran Yenileme Hizi : {}".format(self.name,self.ram,self.ssd,self.islemci,self.ekran_karti,self.hz)
    
bilgisayar = Bilgisayar("DELL",16,512,"i5 12500H","RTX 3050","120 Hz")
print(bilgisayar)

# class Bilgisayar():
#     def __init__(self,name,ram,ssd,islemci,ekran_karti,hz):
#         self.name = name
#         self.ram = ram
#         self.ssd = ssd
#         self.islemci = islemci
#         self.ekran_karti = ekran_karti
#         self.hz = hz
#     def __len__(self):
#         return self.ram
# bilgisayar = Bilgisayar("DELL",16,512,"i5 12500H","RTX 3050",120)
# print(len(bilgisayar))

