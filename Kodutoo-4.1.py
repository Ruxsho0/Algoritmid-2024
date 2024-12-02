# 1. Räsimise (hashing) kontseptsioon - põhiidee ja eesmärk
# Räsimine on protsess, kus suvalise suurusega sisend (nt. string) teisendatakse fikseeritud suurusega väärtuseks, mida nimetatakse räsi väärtuseks või hash väärtuseks. 
# Räsifunktsioon on matemaatiline funktsioon, mis teostab selle teisenduse. Räsimise eesmärk on võimaldada kiiret andmete otsimist ja võrdlemist,
# kuna fikseeritud suurusega räsi väärtusi on lihtsam hallata ja võrrelda kui algseid andmeid.

# 2. Hea räsifunktsiooni omadused ja nende olulisus
# - Deterministlikkus: Sisend ja väljund peavad olema koguaeg samad.
# - Kiirus: Räsifunktsioon peab olema kiire.
# - Ühtlane jaotus: Räsifunktsioon peab jaotama sisendid ühtlaselt, et vältida kokkupõrkeid.
# - Kokkupõrgete minimeerimine: Hea räsifunktsioon minimeerib kokkupõrgete arvu, kus erinevad sisendid annavad sama räsi väärtuse.

# 3. Kokkupõrgete lahendamise tehnikad
# Kokkupõrge tekib siis, kui kaks erinevat sisendit annavad sama räsi väärtuse. Kokkupõrgete lahendamiseks on mitmeid tehnikaid:

# - Eraldi aheldamine (separate chaining): Selle meetodi puhul hoitakse iga räsi väärtuse jaoks linkide loendit (või mõnda muud andmestruktuuri, nt. puu).
# Kui tekib kokkupõrge, lisatakse uus element lihtsalt loendi lõppu. See meetod on lihtne ja tõhus, kuid võib nõuda täiendavat mälu.

# - Avatud aadresseerimine (open addressing): Selle meetodi puhul hoitakse kõik elemendid samas massiivis ja kokkupõrke korral otsitakse järgmine vaba koht massiivis.
# Avatud aadresseerimise meetodid hõlmavad lineaarset sondimist (linear probing), kvadraatset sondimist (quadratic probing) ja kahendpuu sondimist (double hashing).
# See meetod väldib täiendava mälu kasutamist, kuid võib põhjustada klastrite (clusters) tekkimist, mis võib aeglustada otsingut.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

# Näide

hash_table = HashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
print(hash_table.get("key1"))  
print(hash_table.get("key2"))  
print(hash_table.get("key3"))  