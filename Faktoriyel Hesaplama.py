print("Faktoriyel Hesaplama...")



while True:
    sayi = (input("Sayinizi Giriniz (Cikmak icin 'q' ya basiniz) : "))

    if(sayi == 'q'):
        print("Program sonlandi.")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *= i

        print(faktoriyel)
