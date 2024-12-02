class HashTable:
    def __init__(self, initial_capacity=8):
        self.table = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _rehash(self):                                  # Meetod, et suurendada räsitabeli suurust ja uuesti räsimine
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    def insert(self, key, value):
        if self.size / self.capacity > 0.7:
            self._rehash()

        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity

        self.table[index] = (key, value)
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        return None

# 1. Koormustegur

# Räsitabeli koormustegur (load factor) on määratletud kui elementide arv jagatud tabeli suurusega.
# Koormustegur = number_of_elements / table_size
# See on oluline, sest kõrge koormustegur võib põhjustada rohkem kokkupõrkeid, mis omakorda vähendab räsitabeli jõudlust.
# Madal koormustegur tähendab, et tabelis on palju tühje kohti, mis võib olla mälu raiskamine.

# 2. Rehashingu protsess

# Rehashing on protsess, kus räsitabeli suurust suurendatakse ja kõik olemasolevad elemendid räsitakse uuesti uude tabelisse.
# See aitab säilitada efektiivset räsitabelit, vähendades kokkupõrkeid ja parandades otsinguaega.

# 3. Rehashingu mõju jõudlusele

# Rehashing parandab räsitabeli jõudlust, kuna see vähendab kokkupõrkeid ja hoiab otsingu, lisamise ja kustutamise operatsioonid O(1) ajakompleksuses.
# Siiski on rehashing kallis operatsioon, kuna see nõuab kõigi elementide uuesti räsimist ja kopeerimist uude tabelisse.