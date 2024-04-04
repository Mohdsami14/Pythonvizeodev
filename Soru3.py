A = ("cat", "bird", "dolphin", "giraffe", "elephant", "dog")

en_uzun_kelime = ""
uzunluk = 0

for kelime in A:
    if len(kelime) > uzunluk:
        en_uzun_kelime = kelime
        uzunluk = len(kelime)

print("En uzun kelime:", en_uzun_kelime)
print("Kelimenin uzunluğu:", uzunluk)

