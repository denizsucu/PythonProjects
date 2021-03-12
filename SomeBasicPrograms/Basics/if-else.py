#servis aralığı uygulaması

import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (yyyy/mm/dd): ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigeCikis
days = fark.days

print(days)

if days <= 365:
    print("1. servis aralığı")

elif (days > 365) and (days <= 365*2):
    print("2. servis aralığı")

elif (days > 365*2) and (days <= 365*3):
    print("3. servis aralığı") 

else:
    print("Hatalı servis günü")

# Body Index Uygulaması

name = input("What is your name?")
height = float(input("How tall are you?"))
weight = float(input("What is your weight?"))

index = weight/(height ** 2)

if (index >= 0) and (index <= 18.4):
    print(f"{name}, Zayıf. ")

elif(index > 18.4) and (index <=24.9):
    print(f"{name}, Normal kilo")

elif(index > 24.9) and (index <= 29.9):
    print(f"{name}, Kilolu")

elif(index > 29.9) and (index <= 34.9):
    print(f"{name}, Obez")
elif(index > 35):
    print(f"{name} , aşırı obez")

else:
    print("bilgiler yanlış")


