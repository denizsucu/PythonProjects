#formating
# name = "Deniz"
# age = 22
# print("My name is {} and I'm {} years old.".format(name, age))
# print("My name is {0} and I'm {1} years old.".format(name, age)) #index olarak da verebiliriz
# print("My name is {1} and I'm {0} years old.".format(name, age)) #index kısmı burda daha net
# print("My name is {s} and I'm {n} years old.".format(s = name, n = age)) #bu şekilde değişken de verebiliriz
# print("My name is {n} and I'm {s} years old.".format(s = name, n = age)) #değişken bu örnekle daha net

# result = 200/700
# print("The result is {r:1.4}".format(r=result)) #sol taraf kaç karakterlik yer ayrılacağı, sağ taraf 
#                                                 #virgülden sonra kaç basamak yazılacağını gösteriyor

# #fstring
# print(f"My name is {name} and I'm {age} years old.") #direkt parantezler içine değişken adı yazıp kullanabiliriz

#Uygulama
# website = "www.denizsucu.github.com"
# course = "Python Kursu, sıfırdan ileri seviye"

#Q1: "course" string'inde kaç karakter bulunmaktadır?
#x = len(course)

#Q2: website içerisinden www karakterlerini alın.
# x = website[:3]

#Q3: website içinden com karakterlerini alın
# x = website[-3:]

#Q4: course içinden ilk 15 ve son 15 karakteri alın.
# x = course[:15]
# y = course[-15:]

#Q5: course karakterlerini tersten yazdırın.
# x = course[::-1]

#Q6: "Hello world" ifadesindeki w'yi W yap.
# s = "Hello world"
# x = s.replace("w","W")

#Q7: "abc" ifadesini yan yana 3 defa yazdır.
# x = "abc" * 3

# print(x)
#print(y)

#STRING-METHODS
message = " Hello There. I'm Deniz"
message = message.upper() # bütün harfler, büyük yaptı
message = message.lower() # bütün harfleri küçük yapar
message = message.title() # her kelimenin baş harfi büyük olur
message = message.capitalize() #string'in sadece ilk harfini büyük yapar
message = message.strip() # baş ve sondaki boşluğu siler, parolalarda vs sorun çıkmaması için kullanılabilir
message = message.split() # her bir boşluktan ayrılıp, liste haline getirir, istediğimize ulaşırız burdan
# message = message.split(".") # nokta olan kısımdan itibaren ayırma yapacak
message = " ".join(message) # ayırdığımızı birleştirmek için, boşluk yerine farklı şeyler de koyabiliriz duruma göre değişir o
# index = message.find("deniz") # string içinde bir kelimeyi bulmak için
# print(index) # -1 dönerse bu kelime bu cümle içinde değil demektir

# isFound = message.startswith("h") #string'in h ile başlayıp başlamadığını kontrol ediyor
# isFound = message.endswith("z") # z ile mi bitiyor kontrol etmeye yarıyor
# print(isFound)

message = message.replace("deniz", "Sema")
message = message.replace(" ", "*") #url bilgisi oluştururken vs lazım olabilir

message = message.center(100, "*") # cennter içindeki değer kadar karakterlik alan ayırıp, string'i merkezi hale getirir, kalan kısıma verdiğimiz karakterli koyabilir

print(message)

#UYGULAMA
# 1- " Hello world " string'deki boşlukları sil.
result = " Hello world ".strip()
result = result.lstrip() #soldakini siler
result = result.rstrip() #sağdakini siler
print(result)


