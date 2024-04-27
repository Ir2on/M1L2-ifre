import random
karakterler = "fjdjsjcjcjj37474jdjsjxc54++shchch9588!^'%^/+DHHCHHWOCORKP"
sifre_uzunlugu = int(input("Şifrenin uzunluğunu girin:"))

sifre = ""

for i in range(sifre_uzunlugu):
    sifre = sifre + random.choice(karakterler)

print(sifre)
