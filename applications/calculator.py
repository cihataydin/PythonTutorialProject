print("Lütfen yapılıcak işlemi seçiniz:")
print("-------------------------")
print("1.toplama")
print("2.çıkarma")
print("3.çarpma")
print("4.bölme")

while(True):
    try:
        secim = input("Yapmak istediğiniz işlemin numarasını giriniz:")

        if secim != "1" and secim != "2" and secim != "3" and secim != "4":
            raise TypeError('Hatalı bir işlem kodu girdiniz')           

        sayi1 = int(input("1. Sayı: "))
        sayi2 = int(input("2. Sayı: "))

        if sayi2 == 0 and secim == "4":
            print("girdiğiniz 2. sayı bölme işlemi için geçerli değildir.")
            sayi2 = int(input("2. sayıyı tekrar giriniz:"))

        toplama = sayi1 + sayi2
        çıkarma = sayi1 - sayi2
        çarpma = sayi1 * sayi2
        bölme = sayi1 / sayi2

        if secim == "1":
            print( "işlem sonucunuz = {}".format(toplama))
        elif secim == "2":
            print( "işlem sonucunuz =  {}".format(çıkarma))
        elif secim =="3":
            print ("işlem sonucunuz =  {}".format(çarpma))
        elif secim =="4":
            print ("işlem sonucunuz =  {}".format(bölme))
    except TypeError as error:
        print(error)
    except ValueError as error:
        print("Girdiğiniz değer geçerli bir sayı değildir.")