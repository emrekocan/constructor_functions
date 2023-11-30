import random
class Dusman:


    def __init__(self,isim = "Vatandas",kalan_can = 500,saldırı_gücü = 30, mermi_sayısı = 20):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldırı_gücü = saldırı_gücü
        self.mermi_sayısı = mermi_sayısı
    
    def saldir(self):
        print(self.isim + " saldırıyor.")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " kadar harcandı.")
        self.mermi_sayısı -= harcanan_mermi

        return(harcanan_mermi,self.saldırı_gücü)
    
    def saldiriyaUgra(self,harcanan_mermi,saldırı_gücü):
        print("vuruldum")
        self.kalan_can -= (harcanan_mermi * saldırı_gücü)

    def mermi_bitti_mi(self):
        if (self.mermi_sayısı <= 0):
            print(self.isim + "Konuşuyor: Mermim bitti, çıkıyorum")
            return True
        return False
    def hayatta_mi(self):
        if (self.kalan_can <= 0):
            print("Ölüyorummmmmm...")
            
    def print(self):
        print("Basılıyorrrr...........")
        print("İsim: ",self.isim,"Kalan Can: ",self.kalan_can, "Saldırı Gücü: ",self.saldırı_gücü,"Mermi Sayısı: ",self.mermi_sayısı)

dusmanlar = []

i = 0
while (i < 10 ):
    rastgelecan = random.randrange(100,200)
    rastgelesaldirgucu = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman" + str(i+1),rastgelecan,rastgelesaldirgucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i += 1

i = 0 
while (i < 3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir() # (15,5)


    dusmanlar[randomdusman2].saldiriyaUgra(donendeger[0],donendeger[1])

    print("Round bitti...")

    i +=1