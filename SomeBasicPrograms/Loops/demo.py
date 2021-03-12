# Sayı Tahmin Etme

import random

sayi = random.randint(1,100)

deneme = int(input("deneme hakkı kaç olsun"))

while deneme > 0:
    deneme -=1
    tahmin = int(input("tahmin"))

    if (sayi == tahmin):
        print("tebrikler")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if deneme == 0:
        print(f"hakkınız bitti, sayi= {sayi}") 

# Asal Sayı

sayi = int(input("Sayı giriniz: "))
flag = True

if sayi == 1:
    print("Asal değil.")

for i in range(2, sayi):
    if sayi % i == 0:
        flag=False
        break

if flag==True:
    print("Asal")
else:
    print("Asal değil.")