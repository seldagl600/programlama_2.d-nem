sure=int(input("kaldiğiniz süreyi girin :"))

if sure == 1:
    print("ödenecek tutar 5TL")
elif sure <=5:
    print("ödenecek tutar:",sure * 4)
elif sure >5:
    print("ödenecek tutar:",sure * 3)
else:
    print("hatali giriş")