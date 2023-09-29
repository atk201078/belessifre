import random, time
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
prluzunluk = int(input("Parola karakterini gir: "))
sifre = ""
time.sleep(2)

for i in range(prluzunluk):
    sifre += random.choice(karakter)
    
print("Şifre:",sifre)
