import time

class Hayvan():
    def __init__(self,beslenme,ic_gudu):
        self.beslenme = beslenme
        self.ic_gudu = ic_gudu
    
class Kopek(Hayvan):
    def __init__(self, beslenme, ic_gudu,ayak_sayisi,ses):
        super().__init__(beslenme, ic_gudu)
        self.ayak_sayisi = ayak_sayisi
        self.ses = ses

    def __len__(self):
        return self.ayak_sayisi
    
    def __str__(self):
        print("Kopeklerin Ozellikleri...")

        return "Beslenme : {}\nIc Gudu : {}\nAyak Sayisi : {}\nCikarilan Ses : {}".format(self.beslenme,self.ic_gudu,self.ayak_sayisi,self.ses)

class Kus(Hayvan):
    def __init__(self, beslenme, ic_gudu,ucma,ses):
        super().__init__(beslenme, ic_gudu)
        self.ucma = ucma
        self.ses = ses

    def __str__(self):
        print("Kusun Ozellikleri...")
        return "Beslenme : {}\nIc gudu : {}\nCikarilan Ses : {}".format(self.beslenme,self.ic_gudu,self.ses)
    
class At(Hayvan):
    def __init__(self, beslenme, ic_gudu,ses,nal_sayisi):
        super().__init__(beslenme, ic_gudu)
        self.ses = ses
        self.nal_sayisi = nal_sayisi

    def __len__(self):
        return self.nal_sayisi
    
    def __str__(self):
        print("At Ozellikleri...")
        return "Beslenme : {}\nIc gudu : {}\nCikarilan Ses : {}\nNal Sayisi : {}".format(self.beslenme,self.ic_gudu,self.ses,self.nal_sayisi)
    
kopek = Kopek("Etcildir","Ic Gudulerini kullanir",4,"Hav Hav")
kus = Kus("Daha Cok Otculdur","Ic Gudulerini kullanirlar","Ucma Kabiliyeti Yuksektir","Cik Cik")
at = At("Havuc ve Yulaf severler","Ic Gudulerini kullanirlar","Ai  Ai",4)

print("1 - Kopek Bilgileri")
print("2 - Kus Bilgileri")
print("3 - At Bilgileri")
print("0 - Exit")




while True:
    secim = int(input("Yukaridakilerden birini seciniz : "))
    if(secim == 0):
        break
    elif(secim == 1):
        print("Kopek Bilgileri Veriliyor...")
        time.sleep(0.5)
        print(kopek)
    elif(secim == 2):
        print("Kus Bilgileri Veriliyor...")
        time.sleep(0.5)
        print(kus)
    elif(secim == 3):
        print("At Bilgileri Veriliyor...")
        time.sleep(0.5)
        print(at)
    else:
        print("Yanlis Secim Yaptiniz!")
