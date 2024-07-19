class NotDefteri:
    def __init__(self):
        self.notlar = {}

    def not_ekle(self, baslik, metin):
        self.notlar[baslik] = metin
        print("Not eklendi.")

    def not_listele(self):
        if self.notlar:
            for baslik, metin in self.notlar.items():
                print(f"Başlık: {baslik}")
                print(f"Metin: {metin}")
                print("-" * 20)
        else:
            print("Not defterinizde henüz not bulunmamaktadır.")

    def not_duzenle(self, baslik, yeni_metin):
        if baslik in self.notlar:
            self.notlar[baslik] = yeni_metin
            print("Not düzenlendi.")
        else:
            print("Belirtilen başlıkta bir not bulunamadı.")

    def not_sil(self, baslik):
        if baslik in self.notlar:
            del self.notlar[baslik]
            print("Not silindi.")
        else:
            print("Belirtilen başlıkta bir not bulunamadı.")

def main():
    not_defteri = NotDefteri()

    while True:
        print("""
        Not Defteri Uygulaması
        1. Not Ekle
        2. Notları Listele
        3. Not Düzenle
        4. Not Sil
        5. Çıkış
        """)

        secim = input("Lütfen bir seçim yapın: ")

        if secim == "1":
            baslik = input("Not başlığını girin: ")
            metin = input("Not metnini girin: ")
            not_defteri.not_ekle(baslik, metin)
        elif secim == "2":
            not_defteri.not_listele()
        elif secim == "3":
            baslik = input("Düzenlemek istediğiniz notun başlığını girin: ")
            yeni_metin = input("Yeni metni girin: ")
            not_defteri.not_duzenle(baslik, yeni_metin)
        elif secim == "4":
            baslik = input("Silmek istediğiniz notun başlığını girin: ")
            not_defteri.not_sil(baslik)
        elif secim == "5":
            print("Not defteri uygulamasından çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
