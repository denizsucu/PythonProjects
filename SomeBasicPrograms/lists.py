numbers = [1,1,1,1,2,3,4,78,65,232,23,89]
letters = ["d","f","t","y","p"]

numbers.append(5) # sona eleman ekler
numbers.insert(3,78) # belirli bir indexe eleman ekler

numbers.pop(0) #index verirsek, idex içindeki elemanı, vermezsek en sondaki elemanı silmeye yarar
numbers.remove(78) # içine silmek istediğimiz elemanı veriyoruz

numbers.sort() #sıaralayacak
numbers.reverse() #listeyi tersine çevirir
letters.sort() #alfabetik sıraya göre sıralayacak

# print(numbers)
# print(letters)

# print(len(numbers))
# print(len(letters))

# print(numbers.count(1)) #istediğimiz bir elemanın kaç defa olduğunu  bulabiliriz

# UYGULAMA
names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# names.append("Cenk") # sonuna Cenk ekle

# names.insert(0,"Sena") #listenin basına Sena ekle

# names.remove("Deniz") # Deniz i sil

# print(names.index("Deniz")) # Deniz'in index'i

# print(names.count("Ali")) # Ali bu listenin elemanı mı

names.reverse() #liste elemanlarını ters çevir
years.reverse()
names.sort()
years.sort()

# strX = "Chevrolet, Dacia" #diziye çevir
# x= strX.split(",")
# print(x)

min = min(years) # years içindeki min, max değerler
max = max(years)

print(min)
print(max)

x = years.count(1998) #1998 kaç defa var
print(x)

years.clear() # dizinin bütün elemanlarını siler
print(years)

markalar = []
x = input("marka1?")
markalar.append(x)
y = input("marka2?")
markalar.append(y)
z = input("marka3?")
markalar.append(z)

print(markalar)

#TUPLE
tuple = (1, "iki", 3) #elemanlara herhangi bir atama yapamıyoruz

print(type(tuple))