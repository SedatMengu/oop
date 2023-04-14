class ogrenci:
    pass

ogrenci1=ogrenci()

ogrenci1.name    ="Ali"
ogrenci1.surname ="Veli"
ogrenci1.age     = 24
ogrenci1.sinifi  ="11/B"
ogrenci1.okul_no = 112

print("Öğrencinin Adı           : {} " .format(ogrenci1.name))
print("öğrencinin soyadı        : {} " .format(ogrenci1.surname))
print("ogrencinin yaşı          : {} " .format(ogrenci1.age))
print("Öğrencinin Sınıfı        : {} " .format(ogrenci1.sinifi))
print("Öğrencinin Okul Numarası : {} " .format(ogrenci1.okul_no))

ogrenci2=ogrenci()

ogrenci2.name    ="İdris"
ogrenci2.surname ="Topçu"
ogrenci2.age     = 23
ogrenci2.sinifi  ="11/D"
ogrenci2.okul_no = 143

print("Öğrencinin Adı           : {} " .format(ogrenci2.name))
print("öğrencinin soyadı        : {} " .format(ogrenci2.surname))
print("ogrencinin yaşı          : {} " .format(ogrenci2.age))
print("Öğrencinin Sınıfı        : {} " .format(ogrenci2.sinifi))
print("Öğrencinin Okul Numarası : {} " .format(ogrenci2.okul_no))


# class mantığına aykırı bir çalışma oldu. class ortak özelliği olan değişkenleri gruplamak için kullanılır. 


class ogrenci_sablonu:
    def __init__(self,name,surname,age,sinif,okul_no):
        self.name=name
        self.surname=surname
        self.age=age
        self.sinif=sinif
        self.okul_no=okul_no

ogrenci11 = ogrenci_sablonu("ali","veli",24,"11/B",123)
ogrenci12 = ogrenci_sablonu("idris","topçu",23,"11/D",143)

print(ogrenci11)
print(ogrenci12.name,ogrenci12.surname,ogrenci12.age,ogrenci12.sinif,ogrenci12.okul_no)
