fruits = {"elma", "armut", "muz"} #indexleme yok burada

# her elemandan sadece bir tane var ve sıralı değiller

# print(type(fruits))

#elemanlara ulaşmak için döngüleri kullanabiliriz
for x in fruits:
    print(x) # elemanları yazdıracak bize

fruits.add("portakal") # eleman ekleme

fruits.update(["mango", "uzum", "kiraz"]) #birden fazla eleman eklemek için

fruits.remove("mango") # bir elemanı kaldırmak için
fruits.discard("elma") # bu şekilde de silme işlemi yapabiliriz

fruits.pop() # hangi elemanı sileceğini bilemeyiz, en son diye bir şey yok
fruits.clear() #bütün elemanları silecektir

print(fruits)

myList = [1,2,4,4,5,5,5,6,7,8,1,1,2]

print(set(myList)) # set'e dönüştürme işleminde tekrar edenler yazılmayacak