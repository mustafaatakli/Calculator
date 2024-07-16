import math

hata1 = {"uyarimesaj1":"Bir sayı sıfıra bölünemez!\n"}
hata2 = {"uyarimesaj2":"Negatif sayıların karekökü alınamaz!\n"}
hata3 = {"uyarimesaj3":"Geçersiz bir tuşa bastınız!\nAna menüye yönlendiriliyorsunuz.\n"}

class Hesapla:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
class Karekok:
    def __init__(self, sayi):
        self.sayi = sayi
        
        
class Toplama(Hesapla):
    def hesapla(self):
        return self.sayi1 + self.sayi2
        
class Cikarma(Hesapla):
    def hesapla(self):
        return self.sayi1 - self.sayi2
    
class Carpma(Hesapla):
     def hesapla(self):
         return self.sayi1 * self.sayi2
              
class Bolme(Hesapla): 
    def hesapla(self):
        if self.sayi2 == 0:
            print(hata1["uyarimesaj1"])
        else:
            return self.sayi1 / self.sayi2
        
class Karekokalma(Karekok):
    def __init__(self):
        pass

    def karekok(self, sayi):
        if sayi >= 0:
            return math.sqrt(sayi)
        else:
            print(hata2["uyarimesaj2"])
            return  
               
class Yuzdehesaplama(Hesapla):
    def hesapla(self):
        return self.sayi1 * self.sayi2 / 100
    
class Hafiza:
    def __init__(self):
        self.sonuclar = []
        
    def sakla(self, sonuc):
        self.sonuclar.append(sonuc)
        
    def goster(self):
        return self.sonuclar
    
    def toplam(self):
        return sum(self.sonuclar)
    
    def sifirla(self):
        self.sonuclar.clear()
   
    
def sayi_girisi(sayi_numarasi):
    return int(input(f"{sayi_numarasi}. sayıyı giriniz: "))
    
def Calculator():
    hafiza = Hafiza()
    while True:
        print("-*HESAP MAKİNESİ*-")         
        islemturu = input("(1)-Toplama\n(2)-Çıkarma\n(3)-Çarpma\n(4)-Bölme\n(5)-Karekök Alma\n(6)-YüzdeHesaplama\n(yüzdesi alınacak sayı/yüzde değeri)\n(7)-Hafıza Sıfırlama\nYapmak istediğiniz işlem türünün numarasını tuşlayınız: ")
           
        if islemturu == '1':
            sayi1 = sayi_girisi(1)
            sayi2 = sayi_girisi(2)
            sonuc = Toplama(sayi1, sayi2).hesapla()
                  
        elif islemturu =='2':
            sayi1 = sayi_girisi(1)
            sayi2 = sayi_girisi(2)
            sonuc = Cikarma(sayi1, sayi2).hesapla()
          
        elif islemturu == '3':
            sayi1 = sayi_girisi(1)
            sayi2 = sayi_girisi(2)
            sonuc = Carpma(sayi1, sayi2).hesapla()
            
        elif islemturu == '4':
            sayi1 = sayi_girisi(1)
            sayi2 = sayi_girisi(2)
            sonuc = Bolme(sayi1, sayi2).hesapla()
            
        elif islemturu == '5':
            sayi = float(input("Bir sayı giriniz: "))
            hesaplayici = Karekokalma()
            sonuc = hesaplayici.karekok(sayi)
            print(f"{sayi} sayısının karekökü: {sonuc}'dir.")  
            
        elif islemturu == '6':
            sayi1 = sayi_girisi(1)
            sayi2 = sayi_girisi(2)
            sonuc = Yuzdehesaplama(sayi1, sayi2).hesapla()
            
        elif islemturu == '7':
            hafiza.sifirla()
            print("Hafıza sıfırlama işlemi başarılı!")
            continue
        
        else:
            print(hata3["uyarimesaj3"])
            continue
        
        hafiza.sakla(sonuc)
        print("cevap: ",sonuc)
        
        devam = input("Devam etmek için 1'i, Çıkış için 0'ı tuşlayınız.\n[GrandTotal için lütfen T'yi tuşlayınız.]\n")
        if devam == '0':
            print("Çıkış işlemi başarılı!")
            break
        
        elif devam == '1':
            continue
        
        elif devam == 'T':
            print(f"Sonuçların toplamı: {hafiza.toplam()}'dir.")
            continue
        
        else:
            print(hata3["uyarimesaj3"])
            continue
           
Calculator()













    
    
        
        
        
    