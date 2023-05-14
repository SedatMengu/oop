class ogrenci:                  # öğrenci adında bir klass oluşturduk ve içerisine herahngi bir şey yazmadık. bu kullanım class mantığına biraz aykırı oldu.
    pass

ogrenci1=ogrenci()

ogrenci1.name    ="Ali"         # bu alanda teker teker class ismine name, surname , age , sinifi , okul_no gibi alanlar tanımladık ve teker teker doldurduk.
ogrenci1.surname ="Veli"        # bu adanlar sadece ogrenci1 için geçerlidir. ogrenci classından bir nesne üretmeye çalışırsak bu name, surname , age , sinifi, okul_no gibi alanlar olmayacak.
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
# bir class a bağlı olan foksiyonlara metot denir.

class ogrenci_sablonu:
    def __init__(self,name,surname,age,sinif,okul_no):      # sablonun içereceği değişkenleri parantez içinde belirtiyoruz.
        self.name=name                                      # self.name parantez içindeki 1.index
        self.surname=surname                                # self.surname parantez içindeki 2.index
        self.age=age                                        # self.age parantez içindeki 3.index
        self.sinif=sinif                                    # self.sinif parantez içindeki 4.index
        self.okul_no=okul_no                                # self.okul_no parantez içindeki 5.index oluyor.
    

ogrenci11 = ogrenci_sablonu("ali","veli",24,"11/B",123)
ogrenci12 = ogrenci_sablonu("idris","topçu",23,"11/D",143)

print(ogrenci11.name,ogrenci11.surname,ogrenci11.age,ogrenci11.sinif,ogrenci11.okul_no)     # bu kadar kod yazacağımıza bunu da class içine gömerek her defasında teker teker yazmaktan kurtulabiliriz.
print(ogrenci12.name,ogrenci12.surname,ogrenci12.age,ogrenci12.sinif,ogrenci12.okul_no)     # bu kadar kod yazacağımıza bunu da class içine gömerek her defasında teker teker yazmaktan kurtulabiliriz. 


# şablon dosyamız içinde birtane metot yazarak değişkenlerin tamamını yazdırmayı da otomatik hale getirebiliriz.

class ogrenci_sablonu:
    def __init__(self,name,surname,age,sinif,okul_no):      # sablonun içereceği değişkenleri parantez içinde belirtiyoruz.
        self.name=name                                      # self.name parantez içindeki 1.index
        self.surname=surname                                # self.surname parantez içindeki 2.index
        self.age=age                                        # self.age parantez içindeki 3.index
        self.sinif=sinif                                    # self.sinif parantez içindeki 4.index
        self.okul_no=okul_no                                # self.okul_no parantez içindeki 5.index oluyor.
    def show_info(self):                                    # bir class a bağlı olan fonksiyonlara metot denir. metot çağırılanca ne yapacağınız aşağıda belirttik.
        print("isim : {}  soyisim : {} yaş : {}  sınıf : {}  okul no {}".format(self.name,self.surname,self.age,self.sinif,self.okul_no))

ogrenci11.show_info()
ogrenci12.show_info()


# bazı değişkenleri boş bırakmak isteyebiliriz. 

class calisan:
    def __init__(self,name,surname,age=20):   # bu class dan üretine nesnelerde yaş boş bırakılırsa 20 olarak tanımlı gelecek. sıralı olarak girmek gerekir. 0.index isim , 1.index soyisim , 2.index yaştır. soyisim boş bırakılır ve şablonda default olarak tanımlı değilse hata verir.
        self.name=name
        self.surname=surname
        self.age=age
    def tumunu_goster(self):
        print("Personel isim : {}  , Personel soyisim : {} , Personel Yaşı : {}".format(self.name,self.surname,self.age))

calisan1=calisan("Kelam","Kaçmaz",34)

calisan1.tumunu_goster()

# girdiğim personelin soyadı yoksa 

calisan2 = calisan("ahmet","büyük")
calisan2.tumunu_goster()               # / Personel isim : ahmet  , Personel soyisim : büyük , Personel Yaşı : 20 (20 yaş default olarak ayarlandı) 


class calisan_2:
    def __init__(self,name,surname="girilmedi",age=20):   # bu class dan üretine nesnelerde yaş boş bırakılırsa 20 , soyisim boş bırakılırsa "girilmedi" olarak tanımlı gelecek. sıralı olarak girmek gerekir. 0.index isim , 1.index soyisim , 2.index yaştır. soyisim boş bırakılır ve şablonda default olarak tanımlı değilse hata verir.
        self.name=name
        self.surname=surname
        self.age=age
    def tumunu_goster(self):
        print("Personel isim : {}  , Personel soyisim : {} , Personel Yaşı : {}".format(self.name,self.surname,self.age))

personel1 = calisan_2("cemal",34)
personel1.tumunu_goster()                   # / Personel isim : cemal  , Personel soyisim : 34 , Personel Yaşı : 20 (girilen verilerden birinci birinciye , ikinci ikinciye , üçüncü üçüncüye,)


# class veriables , instance veriables

class calisan3:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
    
mudur = calisan3("Kemal","Erkek",15000)
mudur_yard = calisan3("veli","Kaçar",10000)

print(mudur.__dict__)                       # / {'ad': 'Kemal', 'soyad': 'Erkek', 'maas': 15000} dictionary olarak çıktı verdi.
print(mudur_yard.__dict__)                  # / {'ad': 'veli', 'soyad': 'Kaçar', 'maas': 10000} dictionary olarak çıktı verdi.

# yukarıdaki instance da girilen kemal , veli , erkek , kaçar , 15000 , 10000 instance veriables örnekleridir.


class calisan3:
    zam_orani=1.1                           # bu class dan türetilen bütün nesnelerde bu değişken tanımlı olacak.
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas

calisan99 = calisan3("ali","kemal",5000)
calisan09 = calisan3("idris","çam",4000)
print(calisan99.zam_orani)              # türetilen nesneden zam oranına erişim mevcut.
print(calisan3.zam_orani)               # class ın kenisinden zam oranına erişim mevcut.
print(calisan99.__dict__)               # türetilen nesnenin dict inde görünmez,
print(calisan3.__dict__)                # class ın kendi dict inde görünür.

calisan99.zam_orani=1.3
print(calisan99.zam_orani)              # turetilen nesneden zam oranını değiştirirsek sadece türetilen nesne etkilenir. (1.3 oldu)
print(calisan09.zam_orani)              # turetilen nesneden zam oranını değiştirirsek sadece türetilen nesne etkilenir. (1.3 olmadı)
print(calisan3.zam_orani)               # turetilen nesneden zam oranını değiştirirsek sadece türetilen nesne etkilenir. (1.1 de kaldı)
print(calisan99.__dict__)               # yapılan değişiklik dict de göründü
print(calisan09.__dict__)               # yapılan değişiklik dict de görünmedi
print(calisan3.__dict__)                # yapılan değişklik dict de görünmedi , ilk tanımlı olan dict te görünüyor.

calisan3.zam_orani=1.5

print(calisan09.zam_orani)              # class ın zam oranını değiştirirsek türetilen nesneler de etkilenir ( 1.5 oldu)
print(calisan99.zam_orani)              # class ın zam oranını değiştirdik ancak 99 nolu çalışanın zam oranını bireysel olarak değiştirdiğimizden onda bir değişiklik olmdı ( 1.3 de kaldı)
print(calisan3.zam_orani)               # class ın zam oranını değiştirirsek türetilen nesneler de etkilenir ( 1.5 oldu)
print(calisan09.__dict__)               # yapılan değişklik dict te görünmedi.
print(calisan99.__dict__)               # yapılan değişklik dict te güncellenmedi (1.3 olarak görünüyor)
print(calisan3.__dict__)                # yapılan değişiklik dict te güncellendi.


# her personel kaydında personel sayısının 1 artmasını istiyoruz diyelim.

class calisan4:
    personel_sayisi=1                        
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        calisan4.personel_sayisi += 1


print(calisan4.personel_sayisi)
calisan41= calisan4("Ali","Veli",5000)
print(calisan4.personel_sayisi)
calisan42=calisan4("leman","kuş",7000)
print(calisan4.personel_sayisi)
calisan43=calisan4("sevilay","uzun",7500)
print(calisan4.personel_sayisi)



# class metotları , instance metotları , static metotlar

class calisan5:
    zam_orani = 1.1                                 # / class veriable
    kisi_sayisi=0                                   # / class veriable
    def __init__(self,isim,soyisim,meslek):
        self.isim=isim                              # / instance veriable
        self.soyisim=soyisim                        # / instance veriable
        self.meslek=meslek                          # / instance veriable
        calisan5.kisi_sayisi += 1
    def bilgileri_soyle(self):                      # / parantez içine self aldığı için instance metot denir.
        return ("isim :  {} , soyisim : {} , meslek : {}".format(self.isim,self.soyisim,self.meslek))
    
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi

calisan51=calisan5("İdris","Topçu","Öğretmen")
calisan52=calisan5("kemal","topal","mühendis")
calisan53=calisan5("ali","ihsan","memur")

print(calisan51.bilgileri_soyle())              # / isim :  İdris , soyisim : Topçu , meslek : Öğretmen
print(calisan52.bilgileri_soyle())              # / isim :  kemal , soyisim : topal , meslek : mühendis
print(calisan53.bilgileri_soyle())              # / isim :  ali , soyisim : ihsan , meslek : memur
# print(calisan5.bilgileri_soyle())             # / TypeError: bilgileri_soyle() missing 1 required positional argument: 'self' ( instance metot olduğu için hata verdi)


print(calisan5.kisi_sayisini_soyle())           # / 3 

# bir veri tabanına veri kaydetmemiz gerekiyor ancak ihtiyacımız olan veriler bize istediğimiz tarzda gelmeyebilir.
# istediğimiz formata çeirebilmek için class metot kullanabiliriz.
# şablon dosyamızda isim,soyisim,meslek ancak başka bir yerden daha farklı formatlarda dosya gelebilir.