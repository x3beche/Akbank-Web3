from uuid import uuid4
from time import time

class Arac:
    def __init__(self, isim, soyisim, aracin_sinifi, bakiye):
        self.hgs_numarasi   = uuid4().hex
        self.isim           = isim
        self.soyisim        = soyisim
        self.aracin_sinifi  = aracin_sinifi
        self.bakiye         = bakiye
        self.gecis_saatleri = []

class Gise:
    def __init__(self):
        self.birinci_sinif_ucret = 50
        self.ikinci_sinif_ucret  = 100
        self.ucuncu_sinif_ucret  = 150
        self.gecis_yapanlar      = []

    def odeme(self, arac):
         if arac.aracin_sinifi   == 1: gecis_ucreti = self.birinci_sinif_ucret
         elif arac.aracin_sinifi == 2: gecis_ucreti = self.ikinci_sinif_ucret
         elif arac.aracin_sinifi == 3: gecis_ucreti = self.ucuncu_sinif_ucret
         else: return None

         arac.bakiye -= gecis_ucreti

         gecis_aktivitesi = {
            'gecis_yapan_arac'    : arac,
            'gecis_yapilan_zaman' : int(time()),
            'gecis_ucreti'        : gecis_ucreti
         }

         self.gecis_yapanlar.append(gecis_aktivitesi)
         
class Yonetim:
    def gunlukBakiyeHesaplayici(self, gise):
        simdiki_zaman = int(time())
        gunluk_bakiye = 0
        zaman_asimi   = 24*60*60
        for gecis in gise.gecis_yapanlar:
            if gecis['gecis_yapilan_zaman'] + zaman_asimi > simdiki_zaman :
                gunluk_bakiye += gecis['gecis_ucreti']
        return gunluk_bakiye

    def gunlukRapor(self, gise):
        gunluk_bakiye = self.gunlukBakiyeHesaplayici(gise)
        print(f'Gunluk Bakiye : {gunluk_bakiye}')

if __name__ == '__main__':
    
    # yönetim ve gisenin olusturulması
    yonetim = Yonetim()
    gise    = Gise()

    # aracların oludturulması
    arac1 = Arac("Sevde", "Gul",    1, 425)
    arac2 = Arac("Sine",  "Aksu",   1, 800)
    arac3 = Arac("Emre",  "Baris",  2, 5500)
    arac4 = Arac("Serra", "Adamis", 3, 310)

    # gise ödemeleri
    gise.odeme(arac1)
    gise.odeme(arac1)
    gise.odeme(arac1)
    gise.odeme(arac2)
    gise.odeme(arac3)
    gise.odeme(arac4)

    # günlük raporun alınması
    yonetim.gunlukRapor(gise)