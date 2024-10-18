def binaarne_otsing(arr, sihtmärk):
    vasak, parem = 0, len(arr) - 1 # määrab vasaku ja parema piiri

    while vasak <= parem: # kuni vasak piir on väiksem või võrdne parema piiriga
        kesk = (vasak + parem) // 2 # määrab keskpunkti
        if arr[kesk] == sihtmärk: # kui keskpunkti väärtus on sihtmärk
            return kesk # tagastab keskpunkti indeksi
        elif arr[kesk] < sihtmärk: # kui keskpunkti väärtus on väiksem sihtmärgist
            vasak = kesk + 1 # jätkab otsingut parempoolses osas
        else:
            parem = kesk - 1 # jätkab otsingut vasakpoolses osas

    return -1 # tagastab -1, kui sihtmärki ei leitud

# Näide kasutamisest
arr = [1, 3, 5, 7, 9, 11, 13, 15]
sihtmärk = 7
tulemus = binaarne_otsing(arr, sihtmärk)

if tulemus != -1:
    print(f"Element leiti indeksil {tulemus}")
else:
    print("Elementi ei leitud")

# Funktsioon binaarne_otsing otsib sorteeritud täisarvude loendist arr täisarvu sihtmärk.
# Tagastab indeksi, kui sihtmärk leitakse, või -1, kui sihtmärk puudub.
# Algoritm jagab loendi pooleks ja võrdleb keskpunkti väärtust sihtmärk väärtusega.
# Kui keskpunkti väärtus on väiksem, jätkatakse otsingut parempoolses osas.
# Kui keskpunkti väärtus on suurem, jätkatakse otsingut vasakpoolses osas.
# Protsessi korratakse, kuni sihtmärk leitakse või kõik elemendid on läbi otsitud.