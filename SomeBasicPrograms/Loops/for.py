#list için
numbers = [1, 2, 3, 4, 5]

for num in numbers: #numbers içindeki sayıları bastıracak
    print(num)

#string için
name = "deniz sucu"

for n in name:
    print(n) # her karakteri yazdıracak

#tuple için
tuple = ((1,2), (3,4), (5,6))

for t in tuple:
    print(t) # elemanları (x,y) şeklinde yazar

for a,b in tuple:
    print(a,b) # elemanları x y olarak yazar

for a, b in tuple:
    print(b) # a'ya karşılık gelen b'leri yazar

#dictionary için
d = {"k1":1, "k2":2, "k3":3}

for item in d:
    print(item) # diğerlerinde elemanları olduğu gibi yazmıştı ama burda sadece key yazdı

for item in d.items():
    print(item) # bu şekilde eleman grupları şeklinde yazılır

for key, value in d.items():
    print(key,value) # key value şeklinde yazılır

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

#sayilarin toplamı
toplam = 0
for i in sayilar:
    toplam=toplam+i
print(toplam)

#tek sayilarin karesi
for i in sayilar:
    if(i%2 == 1):
        print(i**2)