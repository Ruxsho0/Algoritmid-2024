"""
See funktsioon rakendab AVL-puu, mis on isetasakaalustuv binaarne otsingupuu, kus vasaku ja parema alampuu kõrguste vahe ei tohi ühelgi sõlmel olla suurem kui üks.

AVL-puu peamised omadused:
- Tasakaalutegur: Iga sõlme puhul ei tohi vasaku ja parema alampuu kõrguste vahe olla suurem kui 1.
- Rotatsioonid: Tasakaalu säilitamiseks teostavad AVL-puud rotatsioone (vasak, parem, vasak-parem ja parem-vasak).
- Aegade keerukus: AVL-puud tagavad O(log n) aja keerukuse otsingu, lisamise ja kustutamise operatsioonide jaoks.

AVL-puu tagab, et puu jääb tasakaalu pärast iga lisamis- või kustutamisoperatsiooni, säilitades seeläbi puu logaritmilise kõrguse.
"""
# ---------------------------------------------------------------------------------------------------------------------
"""
Punase-musta puu on isetasakaalustuv binaarne otsingupuu, kus igal sõlmel on värv (punane või must) ja puu järgib teatud reegleid, et tagada tasakaal.

Punase-musta puu peamised omadused:
- Iga sõlm on kas punane või must.
- Juur on alati must.
- Kõik lehed (null-sõlmed) on mustad.
- Kui sõlm on punane, siis mõlemad tema lapsed peavad olema mustad (ei tohi olla kaks järjestikust punast sõlme).
- Iga sõlmest lähtuv tee kuni selle järeltulijateni sisaldab sama arvu musti sõlmi.

Punase-musta puu tagab, et puu jääb tasakaalu pärast iga lisamis- või kustutamisoperatsiooni, säilitades seeläbi puu logaritmilise kõrguse.
"""
# ---------------------------------------------------------------------------------------------------------------------
# AVL puu ja punase-musta puu tõhususe võrdlus
# - AVL puu on üldiselt tasakaalustatum kui punase-musta puu, mis tähendab, et otsingu operatsioonid on kiiremad AVL puus.
# - AVL puu lisamise ja kustutamise operatsioonid võivad olla aeglasemad kui punase-musta puus, kuna AVL puu nõuab rohkem rotatsioone tasakaalu säilitamiseks.
# - Punase-musta puu lisamise ja kustutamise operatsioonid on üldiselt kiiremad, kuna need nõuavad vähem rotatsioone.

# Rakendused ja eelistused
# - AVL puu on eelistatav rakendustes, kus otsingu operatsioonid on sagedasemad kui lisamise ja kustutamise operatsioonid,
# näiteks andmebaasides ja sõnastikes.
# - Punase-musta puu on eelistatav rakendustes, kus lisamise ja kustutamise operatsioonid on sagedasemad,
# näiteks dünaamilistes andmestruktuurides ja reaalajas süsteemides.