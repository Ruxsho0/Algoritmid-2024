# Dijkstra Algoritmi Teoreetiline Analüüs

# Dijkstra algoritm on graafiteoorias kasutatav algoritm, mis leiab lühima tee alguspunktist kõigi teiste punktideni kaalutud graafis.
# Algoritm töötab ainult mitte-negatiivsete kaaludega graafides ja kasutab prioriteetset järjekorda, et valida järgmine uuritav tipp.

# -------------------------------------------------------------------------------------------------------------------------------

# Algoritmi kirjeldus:
# 1. Alguspunkti kaugus iseendast on 0 ja kõigi teiste tippude kaugus on lõpmatus.
# 2. Kõik tipud lisatakse prioriteetsesse järjekorda, kus alguspunkt on esimesena.
# 3. Kuni järjekord pole tühi, võetakse järjekorra esimesena olev tipp ja uuritakse selle naabreid.
# 4. Kui naabri kaugus läbi uuritava tipu on väiksem kui praegune teadaolev kaugus, uuendatakse naabri kaugust ja lisatakse see uuesti järjekorda.
# 5. Protsessi korratakse, kuni kõik tipud on uuritud.

# -------------------------------------------------------------------------------------------------------------------------------

# Algoritmi efektiivsus:
# Dijkstra algoritm on eriti efektiivne, kui:
# - Graaf on hõre (st. tippude arv on palju suurem kui servade arv).
# - Graafis on palju tippe, kuid suhteliselt vähe ühendusi.
# - Kasutatakse prioriteetset järjekorda, mis võimaldab kiiret ligipääsu järgmisele uuritavale tipule (nt. min-heap).

# -------------------------------------------------------------------------------------------------------------------------------

# Algoritmi ebaefektiivsus:
# Dijkstra algoritm võib olla ebaefektiivne, kui:
# - Graaf on tihe (st. servade arv on lähedane tippude arvu ruudule).
# - Graafis on negatiivsed kaalud (sellisel juhul tuleb kasutada Bellman-Fordi algoritmi).
# - Graafis on palju ühendusi, mis muudab prioriteetse järjekorra haldamise kulukaks.