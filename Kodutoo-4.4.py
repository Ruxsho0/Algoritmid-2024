# Avatud aadressimine on meetod kokkupõrgete lahendamiseks räsitabelites, kus kõik elemendid
# salvestatakse samasse tabelisse. Kui räsifunktsioon määrab elemendi juba hõivatud positsioonile,
# otsitakse uus vaba koht vastavalt teatud reeglitele (otsingutehnikale).






# Lineaarne otsing (linear probing):

# Kui kokkupõrge tekib, otsitakse järgmine vaba koht järjestikku (i+1, i+2, i+3, ...).
# Lihtne teostada, kuid võib põhjustada klastrite moodustumist (primary clustering).

# Primary clustering on olukord, kus elemendid kipuvad kogunema samadesse kohtadesse, mis võib aeglustada otsingut.



# Ruuduline otsing (quadratic probing):

# Kui kokkupõrge tekib, otsitakse järgmine vaba koht ruudulise funktsiooni järgi (i+1^2, i+2^2, i+3^2, ...).
# Vähendab klastrite moodustumist, kuid võib põhjustada sekundaarset klastrit (secondary clustering).

# Secondary clustering on olukord, kus elemendid kipuvad kogunema teatud vahemikele, mis võib samuti aeglustada otsingut.



# Topelträsimine (double hashing):

# Kasutab kahte erinevat räsifunktsiooni. Kui kokkupõrge tekib, määratakse uus koht teise räsifunktsiooni abil.
# Väldib klastrite moodustumist, kuid vajab kahte räsifunktsiooni ja võib olla keerulisem teostada.



# Kokkuvõte:

# Lineaarne otsing on efektiivne, kui räsitabel on hõredalt täidetud ja kokkupõrkeid esineb harva.
# Ruuduline otsing on efektiivne, kui soovitakse vältida klastrite moodustumist ja tabeli täituvus on mõõdukas.
# Topelträsimine on efektiivne, kui on vaja minimeerida klastrite moodustumist ja tabeli täituvus on kõrge.