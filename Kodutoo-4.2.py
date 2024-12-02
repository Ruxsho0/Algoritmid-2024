def index_mapping(arr):
    
    max_val = max(arr)                  # Leida massiivi maksimaalne väärtus
    hash_table = [0] * (max_val + 1)    # Loome räsitabeli suurusega max_val + 1
    
    for num in arr:                     # Täida räsitabel
        hash_table[num] = 1
    
    return hash_table

# Funktsioon, et kontrollida, kas element eksisteerib massiivis, kasutades räsitabelit
def exists(hash_table, num):
    if num < len(hash_table) and hash_table[num] == 1:
        return True
    return False

# Näide
arr = [1, 3, 5, 7, 9]
hash_table = index_mapping(arr)

# Kontrolli, kas teatud elemendid eksisteerivad massiivis
print(exists(hash_table, 3))    # Tõene
print(exists(hash_table, 4))    # Väär
print(exists(hash_table, 7))    # Tõene
print(exists(hash_table, 10))   # Väär

"""
Ajakompleksus:

    O(n), kus n on sisendmassiivi elementide arv.
    See on sellepärast, et me läbime massiivi korra, et leida maksimaalne väärtus,
    ja veel korra, et räsitabelit täita.

Ruumikompleksus:

    O(m), kus m on sisendmassiivi maksimaalne väärtus.
    See on sellepärast, et me loome räsitabeli suurusega max_val + 1.
"""


"""
Reaalse maailma rakendused:

Veebisait, kus kasutajad saavad registreeruda oma e-posti aadressiga.
Iga e-posti aadress oleks unikaalne ja et kasutajad ei saaks registreeruda
sama e-posti aadressiga mitu korda. Saab kasutada indeksi kaardistamist, et luua räsitabel,
mis salvestab kõik registreeritud e-posti aadressid ja võimaldab kiiret kontrolli,
kas e-posti aadress on juba kasutusel.
"""