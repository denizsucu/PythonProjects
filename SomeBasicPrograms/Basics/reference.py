# reference types => list, class

a = ["xyz", "abc"]
b = ["xyz", "abc"]

a = b # aynı adresi işaret etmiş oluyorlar

b[0] = "sjgdhsgd" # ikisinin de içeriği değişti

print(a,b)

# OPERATORS

# Atama Operatörleri
x, y, z = 5, 10, 15

x, y = y, x # içerikleri değişir

x += 5 # x = x + 5 => -,*, /, % için de geçerli

#x = x % 5 
x //= 5 # sadece tam kısımla ilgilenirsek

x = x ** 3 # üssünü alıyor

print(x)

values = 1, 2, 3
print(values)
print(type(values))

a, b, c = values
print(a, b, c)

numbers = [1, 2, 3, 5, 7, 6]
aa, *bb, cc = numbers # aa ilk elemanı, cc son elemanı *bb aradaki bütün elemanları alır

print(*bb)

#Karşılaştırma Operatörleri

a, b, c, d = 5, 5, 10, 4

result = (a == b) #True , !=, <, >, <=, >= hepsi aynı

result = (a == c) #False

print(result)

# Logical Operatörler

x = 8

#and
result = (x > 5) and (x < 10) #True  #true, true => true

#or
result = (x > 0) or (x % 2 == 0) # True  #false, false => false,  diğerleri true

#not
result = not(x>0) 

print(result)

#Other Operators

#Identity Operator => is => aynı obje mi buna bakıyoruz
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y)
print(x == z)
print(x is y)
print(x is z) # değerleri önemli değil, değerleri aynı olsa da is operatörü için false oldu

#Membership Operator => in 
x = ["banana", "apple"]
print("banana" in x) # banana x içerisinde var true dönecek

name = "deniz"
print("e" in name) #True
print("e" not in name) #Bu şekilde tersten de sorabiliriz

