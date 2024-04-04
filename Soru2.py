liste1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
öğrenci_numarası = 123456789  # Öğrenci numaranızın tamamını buraya girin

# Öğrenci numarasının son 3 her alıyorum
son_üç_hane = öğrenci_numarası % 1000

# Yeni liste
yeni_liste = liste1[:]
yeni_liste[2][2].append(son_üç_hane)

# Yeni görüntülüyoruz
print("Yeni liste görüntüsü:")
print(yeni_liste)
