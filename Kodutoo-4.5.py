class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.prime = self._get_prime_less_than_size()

    def _hash1(self, key):
        return key % self.size

    def _hash2(self, key):
        return self.prime - (key % self.prime)

    def _get_prime_less_than_size(self):                                    # Meetod, et leida tabeli suurusest väiksem esimene algarv
        for num in range(self.size - 1, 1, -1):                             # Alustame tabeli suurusest - 1 ja liigume tagurpidi
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):    # Kontrollime, kas number on algarv
                return num                                                  # Kui leime algarvu, tagastame selle
        return 3                                                            # Kui ei leia, tagastame 3

    def insert(self, key, value):
        index = self._hash1(key)
        step_size = self._hash2(key)
        while self.table[index] is not None:
            index = (index + step_size) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash1(key)
        step_size = self._hash2(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step_size) % self.size
        return None

    def delete(self, key):
        index = self._hash1(key)
        step_size = self._hash2(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + step_size) % self.size
        return False

# Näide
hash_table = DoubleHashingHashTable(13)
hash_table.insert(10, 'Value1')
hash_table.insert(23, 'Value2')
hash_table.insert(36, 'Value3')

print(hash_table.search(23))  # Value2
print(hash_table.search(36))  # Value3
print(hash_table.search(10))  # Value1

hash_table.delete(23)
print(hash_table.search(23))  # None


# Esmane räsimisfunktsioon (_hash1): See funktsioon määrab algse indeksi võtme põhjal.

# Kokkupõrgete lahendamine (_hahs2): Kui tekib kokkupõrge (st arvutatud indeks on juba hõivatud),
# pakub teisene räsimisfunktsioon sammu suuruse, et leida järgmine saadaval olev indeks.

# Kasutades kahte räsimisfunktsiooni, vähendab topelt räsimine klasterdamise probleemi, mis võib tekkida ühe räsimisega,
# kus mitu võtit räsitakse samale indeksile või lähedastele indeksitele.

# See muudab räsitabeli tõhusamaks ja vähendab pikkade kokkupõrgete ahelate tõenäosust.

"""
Ajakompleksus:
    Sisestamine (insert): Keskmine ja parim ajakompleksus on O(1), kuna topelt räsimine aitab hajutada võtmeid ühtlaselt ja vähendab kokkupõrgete arvu.
    Halvimal juhul, kui on palju kokkupõrkeid, võib ajakompleksus olla O(n), kus n on tabeli suurus.
    Otsimine (search): Keskmine ja parim ajakompleksus on O(1). Halvimal juhul, kui on palju kokkupõrkeid, võib ajakompleksus olla O(n).
    Kustutamine (delete): Keskmine ja parim ajakompleksus on O(1). Halvimal juhul, kui on palju kokkupõrkeid, võib ajakompleksus olla O(n).

Ruumikompleksus:
    Ruumikompleksus on O(n), kus n on tabeli suurus, kuna tabeli suurus määrab, kui palju elemente saab tabelisse salvestada.



Topelt räsimine on eriti efektiivne stsenaariumides, kus on suur tõenäosus kokkupõrgeteks, näiteks:
    Kui võtmed on jaotatud ebaühtlaselt ja on palju korduvaid võtmeid.
    Kui tabeli suurus on suhteliselt väike võrreldes sisestatavate võtmete arvuga.
    Kui on vaja vähendada kokkupõrgete arvu ja tagada ühtlane võtmete jaotus tabelis.

Topelt räsimine aitab hajutada võtmeid ühtlasemalt ja vähendab kokkupõrgete arvu, mis omakorda parandab otsimise, sisestamise ja kustutamise toimingute efektiivsust.
"""