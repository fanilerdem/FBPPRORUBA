# Basit bir FBP uygulaması: İki sayıyı toplama

class ToplamaBileseni:
    def __init__(self):
        self.toplam = 0

    def veri_giris(self, sayi):
        self.toplam += sayi

    def veri_cikis(self):
        return self.toplam

class VeriAkisi:
    def __init__(self, bilesen1, bilesen2):
        self.bilesen1 = bilesen1
        self.bilesen2 = bilesen2

    def akis_baslat(self):
        sayi1 = 5
        sayi2 = 10

        self.bilesen1.veri_giris(sayi1)
        self.bilesen2.veri_giris(sayi2)

        sonuc1 = self.bilesen1.veri_cikis()
        sonuc2 = self.bilesen2.veri_cikis()

        print(f"Toplam Sonuç: {sonuc1 + sonuc2}")

# Bileşenleri oluştur
bilesen1 = ToplamaBileseni()
bilesen2 = ToplamaBileseni()

# Veri akışını başlat
veri_akisi = VeriAkisi(bilesen1, bilesen2)
veri_akisi.akis_baslat()