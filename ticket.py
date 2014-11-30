biletSayisi = input("adet")
while biletSayisi > 0:
    if biletSayisi >= 5:
        toplamOdeme = biletSayisi * 1
    elif biletSayisi < 5:
        toplamOdeme = biletSayisi * 3
    print toplamOdeme
    biletSayisi = input("adet")
