print("Lütfen yapılıcak işlemi seçiniz:")
print("-------------------------")
print("1.toplama")
print("2.çıkarma")
secim = input("Seçiminiz iki şeyden oluşuyor...(1 ya da 2):")

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if secim == "1":
    print(sayi1,"+",sayi2,"işlem sonucunuz:", (sayi1+sayi2))
elif secim == "2":
    print(sayi1,"-",sayi2,"işlem sonucunuz:", (sayi1-sayi2))