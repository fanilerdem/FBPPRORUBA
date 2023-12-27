class GirisBileseni:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi

    def dosyayi_oku(self):
        with open(self.dosya_adi, 'r') as dosya:
            metin = dosya.read()
        return metin

class KelimeSayiciBileseni:
    def __init__(self):
        self.kelime_sayisi = 0

    def kelime_say(self, metin):
        kelimeler = metin.split()
        self.kelime_sayisi = len(kelimeler)

    def kelime_sayisini_al(self):
        return self.kelime_sayisi

class CikisBileseni:
    def sonucu_goster(self, kelime_sayisi):
        print(f"Metindeki Kelime Sayısı: {kelime_sayisi}")

class VeriAkisi:
    def __init__(self, giris_bileseni, kelime_sayici_bileseni, cikis_bileseni):
        self.giris_bileseni = giris_bileseni
        self.kelime_sayici_bileseni = kelime_sayici_bileseni
        self.cikis_bileseni = cikis_bileseni

    def akis_baslat(self):
        metin = self.giris_bileseni.dosyayi_oku()
        self.kelime_sayici_bileseni.kelime_say(metin)
        kelime_sayisi = self.kelime_sayici_bileseni.kelime_sayisini_al()
        self.cikis_bileseni.sonucu_goster(kelime_sayisi)

# Bileşenleri oluştur
giris_bileseni = GirisBileseni("ornek_metin.txt")
kelime_sayici_bileseni = KelimeSayiciBileseni()
cikis_bileseni = CikisBileseni()

# Veri akışını başlat
veri_akisi = VeriAkisi(giris_bileseni, kelime_sayici_bileseni, cikis_bileseni)
veri_akisi.akis_baslat()