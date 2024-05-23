
import math
import time

from math import factorial,sqrt,pow

def us_alma(x,y):
    return pow(x,y)
def faktoriyel(x):
    return factorial(x)
def karekok(x):
    return sqrt(x)

def toplama(x,y):
    return x + y
def cikarma(x,y):
    return x - y
def bolme(x,y):
    if y == 0:
        return "Sifira Bolme Hatasi"
    else:
        return x / y
def carpma(x,y):
    return x*y
def us_alma(x,y):
    return pow(x,y)
def karekok(x):
    return math.sqrt(x)
def faktoriyel(x):
    return math.factorial(x)

print("Hesap Makinesi")
print("1. Toplama")
print("2. Cikarma")
print("3. Bolme")
print("4. Carpma")
print("5. Us Alma")
print("6. Karekok Alma")    
print("7. Faktoriyel Alma")

secim = input("Yapmak istediginiz islem nedir (1/2/3/4/5/6/7) : ")

if secim in ["1","2","3","4","5"]:
    a = float(input("Sayiyi Giriniz : "))
    b = float(input("Sayiyi Giriniz : "))

    if(secim == "1"):
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",toplama(a,b))
    elif(secim == "2"):
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",cikarma(a,b))
    elif(secim == "3"):
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",bolme(a,b))
    elif(secim == "4"):
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",carpma(a,b))
    elif(secim == "5"):
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",us_alma(a,b))
else:
    if(secim == "6"):
        c = float(input("Karekokunu almak istediginiz sayiyi giriniz : "))
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",karekok(c))
    elif(secim == "7"):
        d = int(input("Faktoriyelini hesaplamak istediginizi sayiyi giriniz : "))
        print("Islem Yapiliyor...")
        time.sleep(0.5)
        print("Sonuc : ",faktoriyel(d))
    else:
        print("Yanlis Tuslama Yaptiniz !")