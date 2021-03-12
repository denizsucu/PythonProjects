#break and continue

name = 'Deniz Sucu'

for letter in name:
    if letter == 'i':
        break #şart sağlandığında döngüyü durdurur.
    print(letter)

for letter in name:
    if letter == 'i':
        continue #şart sağlandığında şartın olduğu durumu atlayıp devam eder.
    print(letter)

x = 0

while x < 4:
    if x == 3:
        break
        #continue
    print(x)
    x+=1

# DÖNGÜ METOTLARI

#range()
for item in range(10,15,5): #başlangıç-bitiş-artış miktarı (bitiş olan değer sayılmıyor)
    print(item)

#enumarate
greeting = 'hello'
for index, letter in enumerate(greeting):
    print({index}, greeting[index])
    
#zip => index'e göre eşleştirme yapıyor
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(list(zip(list1, list2)))

# LIST CONPREHENSIONS
numbers = [x**2 for x in range(10)] # elemanları sırayla alıp bir liste haline getiriyor
print(numbers)

numbers = [x**2 for x in range(10) if x % 3 == 0]
print(numbers)

#iç içe döngü için
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)