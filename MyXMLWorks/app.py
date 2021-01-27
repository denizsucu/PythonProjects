
"""
    This program is a program that takes information from the user about students and converts it to xml file format.
"""

import xml.etree.ElementTree as ET 
from xml.etree.ElementTree import Element, ElementTree
from xml.dom.minidom import parseString

count = int(input("Kaç öğrenci kaydı gireceksiniz?"))

def GenerateXML(fileName):
    root = ET.Element("Students")
    for i in range(1,count+1):
        stName = input("\n"+ str(i) + ". öğrencinin adını giriniz:")
        stSurname = input(stName + "'nin soy adını giriniz:")
        stAge = input(stName + "'nin yaşını giriniz:")
        stDepartment = input(stName + "'nin bölümünü giriniz:")
        stClass = input(stName + "'nin sınıfını giriniz:")
        stGno = input(stName + "'nin not ortalamasını giriniz:")

        student = ET.Element('student')
        root.append(student)

        stName_tag = ET.SubElement(student, 'stName')
        stName_tag.text = str(stName)

        stSurname_tag = ET.SubElement(student, 'stSurname')
        stSurname_tag.text = str(stSurname)

        stAge_tag = ET.SubElement(student, 'stAge')
        stAge_tag.text = str(stAge)

        stDepartment_tag = ET.SubElement(student, 'stDepartment')
        stDepartment_tag.text = str(stDepartment)

        stClass_tag = ET.SubElement(student, 'stClass')
        stClass_tag.text = str(stClass)

        stGno_tag = ET.SubElement(student, 'stGno')
        stGno_tag.text = str(stGno)

    xml_string = ET.tostring(root)
    dom = parseString(xml_string)

    fileName = dom.toprettyxml(encoding="UTF-8")
    with open("Students.xml", "wb") as f:
        f.write(fileName)

GenerateXML("Students.xml")





        
    
