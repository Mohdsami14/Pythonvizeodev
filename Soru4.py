def pig_latin_cevir(cümle):

    kelimeler = cümle.split()


    for i in range(len(kelimeler)):
        kelime = kelimeler[i]
        ilk_harf = kelime[0]
        kalan_kısım = kelime[1:]
        pig_latin_kelime = kalan_kısım + ilk_harf.lower() + "ay"
        if kelime[0].isupper():
            pig_latin_kelime = pig_latin_kelime.capitalize()
        kelimeler[i] = pig_latin_kelime


    pig_latin_cümle = " ".join(kelimeler)

    return pig_latin_cümle


cümle = input("Lütfen cümleyi girin: ")
print("Pig Latin:", pig_latin_cevir(cümle))
