class GirisBileseni:
    def __init__(self):
        self.n = None

    def giris_al(self):
        self.n = int(input("Fibonacci serisinin kaçıncı terimi hesaplanacak? "))

    def n_al(self):
        return self.n

class HesaplamaBileseni:
    def __init__(self):
        self.fibonacci_sayilari = None

    def fibonacci_hesapla(self, n):
        fibonacci_sayilari = [0, 1]
        for i in range(2, n + 1):
            fibonacci_sayilari.append(fibonacci_sayilari[i - 1] + fibonacci_sayilari[i - 2])
        self.fibonacci_sayilari = fibonacci_sayilari

    def sonuclari_al(self):
        return self.fibonacci_sayilari

class CikisBileseni:
    def sonuclari_goster(self, fibonacci_sayilari):
        print(f"Fibonacci Serisi: {fibonacci_sayilari}")

class VeriAkisi:
    def __init__(self, giris_bileseni, hesaplama_bileseni, cikis_bileseni):
        self.giris_bileseni = giris_bileseni
        self.hesaplama_bileseni = hesaplama_bileseni
        self.cikis_bileseni = cikis_bileseni

    def akis_baslat(self):
        self.giris_bileseni.giris_al()
        n = self.giris_bileseni.n_al()

        self.hesaplama_bileseni.fibonacci_hesapla(n)
        fibonacci_sayilari = self.hesaplama_bileseni.sonuclari_al()

        self.cikis_bileseni.sonuclari_goster(fibonacci_sayilari)

# Bileşenleri oluştur
giris_bileseni = GirisBileseni()
hesaplama_bileseni = HesaplamaBileseni()
cikis_bileseni = CikisBileseni()

# Veri akışını başlat
veri_akisi = VeriAkisi(giris_bileseni, hesaplama_bileseni, cikis_bileseni)
veri_akisi.akis_baslat()