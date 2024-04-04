import numpy as np
from tabulate import tabulate
# Sorduğum daha tecrübeli yazılımcılar bana pandas yerine tabulate ile daha kolay ve daha şık tablo yapabileceğimi söyledi. (haklılarmış)
# Array olan yaşlar
yaslar = np.array([15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65])
# Başlangıç küme merkezleri
c1 = 16
c2 = 22
# Manhattan uzaklık fonksiyonu
def manhattan_uzaklik(x, c):
    return abs(x - c)
# Kümeleme işlemi için fonksiyon
def kumeleme(yaslar, c1, c2, iterasyon_sayisi):
    for i in range(iterasyon_sayisi):
        # Uzaklıkları hesapla
        d1 = manhattan_uzaklik(yaslar, c1)
        d2 = manhattan_uzaklik(yaslar, c2)
        # Kümeleri belirle
        kume1 = yaslar[d1 < d2]
        kume2 = yaslar[d2 <= d1]
        # Yeni küme merkezlerini hesapla
        c1_yeni = np.mean(kume1)
        c2_yeni = np.mean(kume2)
        # Tablo için verileri hazırla
        tablo_verisi = []
        for xi in yaslar:
            dist1 = manhattan_uzaklik(xi, c1)
            dist2 = manhattan_uzaklik(xi, c2)
            nearest_cluster = 1 if dist1 < dist2 else 2
            tablo_verisi.append([xi, c1, c2, dist1, dist2, nearest_cluster, c1_yeni if nearest_cluster == 1 else c2_yeni])
        # Tablo aşaması
        print(f"Iterasyon {i+1}:")
        print(tabulate(tablo_verisi, headers=['xi', 'c1', 'c2', 'Distance1', 'Distance2', 'Nearest Cluster', 'New Centroid'], tablefmt='grid'))
        # Küme merkezlerini yenile
        c1 = c1_yeni
        c2 = c2_yeni

kumeleme(yaslar, c1, c2,4)
# yukardaki son yazan 4 değeri iterasyon sayısını gösterir.
# bu elimizdeki arreylere göre 3. ve 4. tablolar aynıdır.