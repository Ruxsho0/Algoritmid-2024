import heapq

"""
Min-kuhi ja max-kuhi struktuuride teoreetilised omadused:

Min-kuhi:
- Min-kuhi on binaarne puu, kus iga sõlm on väiksem või võrdne oma laste sõlmedega.
- Juursõlm on alati väikseim element.
- Kasutatakse sageli prioriteedi ja Dijkstra algoritmis.

Max-kuhi:
- Max-kuhi on binaarne puu, kus iga sõlm on suurem või võrdne oma laste sõlmedega.
- Juursõlm on alati suurim element.

Aja- ja ruumikomplekssus:

Ajakomplekssus:
- Lisamine (insert): O(log n)
- Väikseima/suurima elemendi eemaldamine (extract-min/extract-max): O(log n)
- Väikseima/suurima elemendi leidmine (get-min/get-max): O(1)

Ruumikomplekssus:
- Kuhja struktuuri hoidmiseks on vaja O(n) ruumi, kus n on elementide arv kuhjas.

Kuhja struktuuride sobivus andmete sorteerimiseks ja prioriteetjärjekordade haldamiseks:

- Min-kuhi sobib hästi prioriteetide haldamiseks, kus väikseim element tuleb kiiresti leida ja eemaldada.
- Max-kuhi sobib hästi sorteerimisalgoritmides, kus suurim element tuleb kiiresti leida ja eemaldada.
- Heapsort kasutab max-kuhja andmete sorteerimiseks O(n log n) ajaga.
- Kuhja struktuurid on efektiivsed, kuna nad võimaldavad kiiret lisamist ja eemaldamist, säilitades samal ajal elementide osalise järjestuse.
"""