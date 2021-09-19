print("Lütfen yapılıcak işlemi seçiniz:")
print("-------------------------")
print("1.toplama")
print("2.çıkarma")

secim = input("Yapmak istediğiniz işlemin numarasını giriniz:")
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

zed = sayi1 + sayi2

if secim == "1":
    print( "işlem sonucunuz = {}".format(zed))
elif secim == "2":
    print( "işlem sonucunuz =  {}".format(zed))