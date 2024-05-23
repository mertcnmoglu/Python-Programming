def dortislem(sayi1,sayi2,islem):
    if(islem == '+'):
        return sayi1+sayi2
    elif(islem == '-'):
        return sayi1-sayi2
    elif(islem == '*'):
        return sayi1*sayi2
    elif(islem == '/'):
        return sayi1/sayi2

islem = input("Islemi giriniz (+ - * /) : ")

sayi1 = int(input("Sayi Giriniz : "))
sayi2 = int(input("Sayi Giriniz : "))

print("Sonucumuz : ",dortislem(sayi1,sayi2,islem))







