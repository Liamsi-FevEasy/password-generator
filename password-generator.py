import random

rastgele = "+-/*!_&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Lütfen şifrenin uzunluğunu giriniz."))

sifre = "" 

for i in range(sifre_uzunlugu):
    sifre += random.choice(rastgele)

print(sifre)
