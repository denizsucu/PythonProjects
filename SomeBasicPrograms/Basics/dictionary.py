# # key - value formatında

# plakalar = {"kocaeli": 41, "istanbul": 34, "ankara": 6, "kilis":79}

# print(plakalar["kilis"]) # value'yu verecek bize

# plakalar["izmir"] = 35 # yeni ekleme yapabiliyoruz

# plakalar["kocaeli"] = "new value" #farklı bir değer atabiliyoruz

# print(plakalar)

users = {
    "deniz": {
        "age":22,
        "email" : "xyz@gmail.com",
        "school": "au"
    },

    "sema": {
        "age":17,
        "email": "zyx@gmail.com",
        "school":"lise"
    }
}

print(users["deniz"])

#UYGULAMA
"""
students = {
    "120":{
        "ad":"Ali"
        "soyad":"Yılmaz"
        "tel":5464846593
    },
    "125": {
        "ad": "Can"
        "soyad": "Korkmaz"
        "tel": 5468773215
    },
    "128":{
        "ad": "Volkan"
        "soyad":"Yükselen"
        "tel":123445567
    }
}
"""
#Kullanıcıdan öğrenci bilgisi alıp, liste içinde tut
students = {}

stNum = input("Student Number: ")
stAd = input("Student Name: ")
stSoyad = input("Student Surname: ")
stTel = input("Tel no: ")

# students[stNum] = {
#     "stAd" : stAd,
#     "stSoyad" : stSoyad,
#     "stTel" : stTel
# }

students.update({
    stNum:{
        "stAd" : stAd,
        "stSoyad" : stSoyad,
        "stTel" : stTel
    }
})

stNum = input("Student Number: ")
stAd = input("Student Name: ")
stSoyad = input("Student Surname: ")
stTel = input("Tel no: ")

students.update({
    stNum:{
        "stAd" : stAd,
        "stSoyad" : stSoyad,
        "stTel" : stTel
    }
})

stNum = input("Student Number: ")
stAd = input("Student Name: ")
stSoyad = input("Student Surname: ")
stTel = input("Tel no: ")

students.update({
    stNum:{
        "stAd" : stAd,
        "stSoyad" : stSoyad,
        "stTel" : stTel
    }
})

stNum = input("Student Number: ")
stAd = input("Student Name: ")
stSoyad = input("Student Surname: ")
stTel = input("Tel no: ")

students.update({
    stNum:{
        "stAd" : stAd,
        "stSoyad" : stSoyad,
        "stTel" : stTel
    }
})


print(students)