# #iki sayı arasındaki tek sayılar
# first = int(input("Birinci Sayı: "))
# second = int(input("İkinci Sayı: "))

# first+=1

# while (first < second):
#     if first % 2 == 1:
#         print(first)
#         first+=2
#     else:
#         print(first+1)
#         first+=2

# #kullanıcıdan sayılar alıp, sıralı yazdır
# n = int(input("Kaç sayı girilecek?"))

# numbers=[]

# i=0
# while i < n:
#     sayi = int(input(f"{i+1}. Sayi:"))
#     numbers.append(sayi)
#     i+=1
# numbers = sorted(numbers)
# print(numbers)  

#Ürünler Listesi
urunler = []

x = int(input("Kaç ürün bilgisi?"))
i=0

while i < x:
    name = input("Ürün adı:")
    price = input("Ürün Fiyatı:")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f"Adı: {urun['name']}, Fiyatı: {urun['price']}")
