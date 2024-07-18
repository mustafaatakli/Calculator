import math

hata1 = {"uyarimesaj1":"Bir sayı sıfıra bölünemez!\n"}
hata2 = {"uyarimesaj2":"Negatif sayıların karekökü alınamaz!\n"}
hata3 = {"uyarimesaj3":"Geçersiz bir tuşa bastınız!\nAna menüye yönlendiriliyorsunuz.\n"}

#işlemler sınıfı
class Calculator:
    #kurucu method
    def __init__(self):
        self.memory = 0

    def toplama(self, x, y):
        sonuc = x + y
        self.memory = sonuc
        return sonuc

    def cikarma(self, x, y):
        sonuc = x - y
        self.memory = sonuc
        return sonuc

    def carpma(self, x, y):
        sonuc = x * y
        self.memory = sonuc
        return sonuc

    def bolme(self, x, y):
        if y != 0:
            sonuc = x / y
            self.memory = sonuc
            return sonuc
        else:
            print(hata1["uyarimesaj1"])
            return

    def karekokhesapla(self, x):
        if x >= 0:
            sonuc = math.sqrt(x)
            self.memory = sonuc
            return sonuc
        else:
            print(hata2["uyarimesaj2"])
            return

    def yuzdehesapla(self, x, y):
        sonuc = x * y / 100
        self.memory = sonuc
        return sonuc

    def reset_memory(self):
        self.memory = 0

    def get_memory(self):
        return self.memory
    
#hafıza sınıfı (tüm sonuçları listede tutup istendiğinde toplayıp verir.) 
class Hafiza:
    def __init__(self):
        self.sonuclar = []
        
    def sakla(self, sonuc):
        self.sonuclar.append(sonuc)
    
    def toplam(self):
        return sum(self.sonuclar)
    
    def sifirla(self):
        self.sonuclar.clear()
        
#input fonk
def kullanici_girisi(islemturu):
    sayi1_input = None
    sayi2_input = None
    
    if islemturu in ['1', '2', '3', '4', '6']:
        sayi1_input = input("Birinci sayıyı giriniz (hafızadaki olan değeri kullanmak için boş bırakın): ")
        sayi2_input = input("İkinci sayıyı giriniz: ")
    elif islemturu == '5':
        sayi1_input = input("Bir sayı giriniz (hafızadaki olan değeri kullanmak için boş bırakın): ")

    # Hafıza
    if sayi1_input == '':
        sayi1 = hesap.get_memory()
    elif sayi1_input is not None:
        sayi1 = float(sayi1_input)
    
    if sayi2_input is not None:
        sayi2 = float(sayi2_input)
    else:
        sayi2 = None
        
    return sayi1, sayi2
    
def main():
    hafiza = Hafiza()
    global hesap
    hesap = Calculator()
    while True:
        print("-*HESAP MAKİNESİ*-")  
        islemturu = input("(1)-Toplama\n(2)-Çıkarma\n(3)-Çarpma\n(4)-Bölme\n(5)-Karekök Alma\n(6)-Yüzde Hesaplama\n(7)-Hafıza Sıfırlama\nYapmak istediğiniz işlem türünün numarasını tuşlayınız: ")
        
        if islemturu not in ['1', '2', '3', '4', '5', '6', '7']:
            print(hata3["uyarimesaj3"])
            continue
        
        if islemturu == '7':
            hafiza.sifirla()
            #hesap.reset_memory()
            print("Hafıza sıfırlandı!")
            continue
        
        
        sayi1, sayi2 = kullanici_girisi(islemturu)
        
        if islemturu == '1':
            sonuc = hesap.toplama(sayi1, sayi2)
            
        elif islemturu == '2':
            sonuc = hesap.cikarma(sayi1, sayi2)
            
        elif islemturu == '3':
            sonuc = hesap.carpma(sayi1, sayi2)
            
        elif islemturu == '4':
            sonuc = hesap.bolme(sayi1, sayi2)
            
        elif islemturu == '5':
            sonuc = hesap.karekokhesapla(sayi1)
            
        elif islemturu == '6':
            sonuc = hesap.yuzdehesapla(sayi1, sayi2)
        
        hafiza.sakla(sonuc)
        print("Sonuç : ",sonuc)

        devam_mi = input("Yeni bir işlem yapmak istiyor musunuz? (evet/hayır): \n[GrandTotal için lütfen T'yi tuşlayınız.]\n")
        if devam_mi == "evet":
            continue
        if devam_mi == "hayır":
            print("Çıkış işlemi başarılı!")
            break
        elif devam_mi == 'T':
            print("Toplam Sonuç: ",hafiza.toplam())
            continue
        else:
            print(hata3["uyarimesaj3"])
            continue

main()

