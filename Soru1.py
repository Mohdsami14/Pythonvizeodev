def yağış_bilgilerini_al():
    yağışlar = []
    for ay in range(1, 13):
        yağış = float(input(f"{ay}. aydaki yağış miktarını giriniz: "))
        yağışlar.append(yağış)
    return yağışlar


def yıllık_toplam(yağışlar):
    return sum(yağışlar)


def aylık_ortalama(yağışlar):
    return sum(yağışlar) / len(yağışlar)


def en_yüksek_ve_en_düşük(yağışlar):
    en_yüksek = max(yağışlar)
    en_düşük = min(yağışlar)
    en_yüksek_ay = yağışlar.index(en_yüksek) + 1
    en_düşük_ay = yağışlar.index(en_düşük) + 1
    return en_yüksek_ay, en_düşük_ay


def main():
    yağışlar = yağış_bilgilerini_al()
    toplam = yıllık_toplam(yağışlar)
    ortalama = aylık_ortalama(yağışlar)
    en_yüksek_ay, en_düşük_ay = en_yüksek_ve_en_düşük(yağışlar)

    print("Yıllık Toplam Yağış Miktarı:", toplam)
    print("Aylık Ortalama Yağış Miktarı:", ortalama)
    print("En yüksek yağış miktarı ayı:", en_yüksek_ay)
    print("En düşük yağış miktarı ayı:", en_düşük_ay)


if __name__ == "__main__":
    main()


