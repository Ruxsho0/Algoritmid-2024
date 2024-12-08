"""
Kirjeldus: 
    Punase-musta puu on binaarne otsingupuu, millel on järgmised omadused:
    1. Iga sõlm on kas punane või must.
    2. Juur on alati must.
    3. Kõik lehed (null-sõlmed) on mustad.
    4. Kui sõlm on punane, siis mõlemad tema lapsed peavad olema mustad (ei tohi olla kahte järjestikust punast sõlme).
    5. Iga sõlmest lähtuv tee kuni selle järeltulijateni sisaldab sama arvu musti sõlmi.

Võrdlus binaarse otsingupuuga:
    - Punase-musta puu kõrgus on alati O(log n), mis tagab, et operatsioonid nagu otsing, lisamine ja kustutamine toimuvad logaritmilise ajaga.
    - Binaarse otsingupuu puhul võib halvimal juhul kõrgus olla O(n), mis muudab operatsioonid lineaarseks.

Tasakaalustamine ja värvireeglid:
    - Punase-musta puu tasakaalustamine toimub värvireeglite ja pööramiste abil, mis tagab, et puu jääb alati tasakaalu.
    - Värvireeglid aitavad hoida puu kõrguse logaritmilisena, mis omakorda tagab operatsioonide tõhususe.
    - Sellepärast seda kutsutakse punase-mustaks puuks.
"""