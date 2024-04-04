def haftalık_satışları_gir():
    satışlar = []  # Satışların gunler
    günler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

    # Her gün için satışları gireck
    for gün in günler:
        satış = float(input(f"{gün} için satış tutarını girin: "))
        satışlar.append(satış)  # Girilen satış tutarını listeye ekle

    return satışlar

def haftalık_toplam_satış(satışlar):
    return sum(satışlar)

def main():

    satışlar = haftalık_satışları_gir()


    toplam_satış = haftalık_toplam_satış(satışlar)


    print("Haftalık Toplam Satış:", toplam_satış)

if __name__ == "__main__":
    main()
