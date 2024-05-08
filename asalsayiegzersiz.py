asalsayi = int(input("Sayiyi giriniz : "))
asalmi = True

if asalsayi == 1:
    print("1 sayisi asal degildir.")

for i in range(2,asalsayi):
    if(asalsayi % i == 0):
        asalmi = False
        break

if asalmi:
    print("Asal sayidir")
else:
    print("Sayi asal degildir")
