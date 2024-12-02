class Node:                                     # Node klassi loomine on vajalik kuna eraldi aheldamise meetod kasutab linked-listi.
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False

# Näide
separate_chaining_ht = SeparateChainingHashTable(10)
open_addressing_ht = OpenAddressingHashTable(10)

# Lisamine
separate_chaining_ht.insert("key1", "value1")
open_addressing_ht.insert("key1", "value1")

# Otsimine
print(separate_chaining_ht.search("key1"))  # value1
print(open_addressing_ht.search("key1"))    # value1

# Kustutamine
separate_chaining_ht.delete("key1")
open_addressing_ht.delete("key1")

print(separate_chaining_ht.search("key1"))  # None
print(open_addressing_ht.search("key1"))    # None

"""
Separate Chaining:

Ajaline komplekssus:
    Keskmine juhtum: O(1) otsing, lisamine ja kustutamine,
    kui räsifunktsioon on hästi jaotatud ja koormustegur on madal.

    Halvimal juhul: O(n) otsing, lisamine ja kustutamine,
    kui kõik võtmed räsitakse samasse ämbrisse (linked-list muutub pikaks).

Ruumiline komplekssus:
    O(n + m), kus n on elementide arv ja m on räsitabeli suurus.
    Iga ämber võib vajada täiendavat mälu linked-listi jaoks.

Open Addressing:

Ajaline komplekssus:
    Keskmine juhtum: O(1) otsing, lisamine ja kustutamine, kui koormustegur on madal.

    Halvimal juhul: O(n) otsing, lisamine ja kustutamine,
    kui tabel on peaaegu täis ja tekib palju kokkupõrkeid.

Ruumiline komplekssus:
    O(m), kus m on räsitabeli suurus.
    Ei vaja täiendavat mälu linked-listide jaoks, kuid vajab suuremat tabelit, et vältida kokkupõrkeid.

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

Plussid:

1. Lihtne rakendada: Separate chaining on lihtne meetod kokkupõrgete lahendamiseks.
2. Dünaamiline suurus: Linked-listid võimaldavad dünaamiliselt kasvada, mistõttu ei ole vaja eelnevalt määrata tabeli suurust.
3. Vähem kokkupõrkeid: Kui räsifunktsioon on hästi jaotatud, on kokkupõrgete arv väike ja linked-listid jäävad lühikeseks.

Miinused:

1. Täiendav mälu: Linked-listid vajavad täiendavat mälu, eriti kui tabel on hõredalt täidetud.
2. Halvimal juhul aeglane: Kui kõik võtmed räsitakse samasse ämbrisse, muutub linked-list pikaks ja ajakompleksus halveneb.
3. Keerukam mälu haldamine: Linked-listide kasutamine võib põhjustada keerukamat mälu haldamist ja prügikoristust.

Separate chaining on hea valik, kui on vaja dünaamilist ja paindlikku räsitabelit,
kuid see võib olla vähem efektiivne mälu kasutamise ja halvimal juhul ajakompleksuse osas võrreldes open addressing meetodiga.

"""








































































































