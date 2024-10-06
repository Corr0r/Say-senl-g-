import random
import time

def oyun_ayarlari(zorluk):
    """Zorluk seviyesine göre sayı aralığını ve tahmin hakkını ayarlayan fonksiyon."""
    if zorluk == '1':
        return 10, 6  # Basit: 1-10 arasında sayı, 6 tahmin hakkı
    elif zorluk == '2':
        return 50, 5  # Orta: 1-50 arasında sayı, 5 tahmin hakkı
    elif zorluk == '3':
        return 100, 4  # Zor: 1-100 arasında sayı, 4 tahmin hakkı
    else:
        print("Geçersiz seçim! Otomatik olarak 'Basit' seçildi.")
        return 10, 6  # Varsayılan olarak basit seviye

def renkli_yaz(metin, renk):
    """Terminalde renkli metin yazdırma."""
    renk_kodlari = {
        'kirmizi': '\033[91m',
        'yesil': '\033[92m',
        'sari': '\033[93m',
        'mavi': '\033[94m',
        'sifirla': '\033[0m'
    }
    print(f"{renk_kodlari[renk]}{metin}{renk_kodlari['sifirla']}")

# Oyun selamlaması ve isim alma
renkli_yaz("Sayı Tahmin Oyununa Hoş Geldiniz!", 'mavi')
isim = input("Lütfen isminizi girin: ")
renkli_yaz(f"Merhaba {isim}! Zorluk seviyesini seçin:", 'sari')
print("1. Basit (1-10 arası)")
print("2. Orta (1-50 arası)")
print("3. Zor (1-100 arası)")

# Zorluk seviyesini alma
zorluk = input("Seçiminiz (1, 2 veya 3): ")
max_sayi, tahmin_hakki = oyun_ayarlari(zorluk)

# Rastgele bir sayı belirle
dogru_sayi = random.randint(1, max_sayi)
renkli_yaz(f"1 ile {max_sayi} arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?", 'yesil')

# Tahmin döngüsü
while tahmin_hakki > 0:
    try:
        tahmin = int(input("Tahmininiz: "))
    except ValueError:
        renkli_yaz("Lütfen geçerli bir sayı girin!", 'kirmizi')
        continue
    
    if tahmin < dogru_sayi:
        renkli_yaz("Daha büyük bir sayı girin.", 'sari')
    elif tahmin > dogru_sayi:
        renkli_yaz("Daha küçük bir sayı girin.", 'sari')
    else:
        renkli_yaz(f"Tebrikler {isim}! {dogru_sayi} sayısını doğru tahmin ettiniz.", 'yesil')
        break
    
    tahmin_hakki -= 1
    renkli_yaz(f"Kalan tahmin hakkınız: {tahmin_hakki}", 'kirmizi')

# Oyunun sonu
if tahmin_hakki == 0:
    renkli_yaz(f"Üzgünüm {isim}, tahmin hakkınız bitti. Doğru sayı {dogru_sayi} idi.", 'kirmizi')

# Oyunun tekrarı
yeniden_oyna = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
if yeniden_oyna == 'e':
    # Tekrar oyunu başlatabiliriz
    exec(open(__file__).read())
else:
    renkli_yaz("Oyun bitti. Teşekkürler!", 'mavi')




 