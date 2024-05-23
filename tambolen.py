def tambolme(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if(sayi %i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("Sayi Girin : ")

    if(sayi == 'q'):
        print("Program Sonlandiriliyor")
        break
    else:
        sayi = int(sayi)

        print("Tam Bolenler : ",tambolme(sayi))  