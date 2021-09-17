# Öncelikle kullanıcıdan değerleri aldık ve 
# input string verdiği için integer a çevirdik.
sayı = int(input("Sayı giriniz lütfen:"))
sayı2= int(input("Sayı giriniz lütfen:"))

# Toplam sonucunu bulduk.
sonuc = sayı + sayı2

# Sonuc değişkeninin değerini inceledik.
if sonuc < 0:
    print("Sonuç: {}. Bu sayı negatiftir.".format(sonuc))
    #print("Sonuç: " + str(sonuc) + ". Bu sayı negatiftir.")
    #print("Sonuç: ", str(sonuc), ". Bu sayı negatiftir.", sep="")
elif sonuc > 0:
    print("Sonuç: {}. Bu sayı pozitiftir.".format(sonuc))
#elif sonuc == 0:
#    print("Sonuc: {}. Bu sayı negatif veya pozitif değildir.".format(sonuc))
else :
    print("Sonuc: {}. Bu sayı negatif veya pozitif değildir.".format(sonuc))