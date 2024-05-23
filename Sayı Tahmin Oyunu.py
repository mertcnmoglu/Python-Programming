import random
import time 

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7

while True:
    tahmin = int(input("Tahmininiz : "))

    if(tahmin < rastgele_sayi):
        print("Bilgiler Sorgulaniyor.")
        time.sleep(1) # Program 1 saniyeliğine durur
        print("Daha Yuksek Sayi Soyleyin")
        tahmin_hakki -= 1
    elif(tahmin > rastgele_sayi):
        print("Bilgiler Sorgulaniyor.")
        time.sleep(1)
        print("Daha Dusuk Sayi Soyleyin")
        tahmin_hakki -= 1
    else:
        print("Bilgiler Sorgulaniyor.")
        time.sleep(1)
        print("Tebrikler! Sayimiz : ",rastgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin Hakkiniz Bitti.")
        print("Sayimiz : ",rastgele_sayi)
        break


        
