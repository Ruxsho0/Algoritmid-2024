'''
Ternary Search on otsingualgoritm, mis töötab sarnaselt kahendotsingule, kuid jagab otsitava ala kolmeks osaks kahe asemel.
Algoritm leiab kaks keskmist punkti ja võrdleb neid otsitava väärtusega, otsustades, millises kolmandikus otsingut jätkata.
See protsess kordub, kuni otsitav väärtus leitakse või otsinguala tühjeneb. 

Pseudo-kood:
function ternarySearch(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return ternarySearch(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternarySearch(arr, mid2 + 1, right, key)
        else:
            return ternarySearch(arr, mid1 + 1, mid2 - 1, key)
    return -1                                                           # kui elementi ei leita
'''
    

    
# Ajaline komplekssus
    # Ternary Search jagab otsitava ala kolmeks osaks ja seega vähendab otsinguala suurust kolmandiku võrra iga sammuga.
    # Selle rekursiivse algoritmi aegkompleksus on O(log3(n)), kus n on elementide arv massiivis.
    # Kuna log3(n) on sama mis log(n) / log(3), siis Ternary Search'i aegkompleksus on O(log(n)) baasilogaritmiga 3.

    # Binary Search jagab otsitava ala kaheks osaks ja seega vähendab otsinguala suurust poole võrra iga sammuga.
    # Selle rekursiivse algoritmi aegkompleksus on O(log2(n)), kus n on elementide arv massiivis.
    # Kuna log2(n) on sama mis log(n) / log(2), siis Binary Search'i aegkompleksus on O(log(n)) baasilogaritmiga 2.

    # Kuigi mõlemal algoritmil on logaritmiline aegkompleksus, on Binary Search tavaliselt kiirem, kuna log2(n) on väiksem kui log3(n).
    # Praktikas tähendab see, et Binary Search teeb vähem võrdlusi ja rekursiivseid kutseid kui Ternary Search sama suurusega massiivi puhul.

    

# Ternary Search vs Binary Search
    # Binary Search on üldiselt tõhusam kui Ternary Search, kuna see vähendab otsinguala suurust poole võrra iga sammuga,
    # samas kui Ternary Search vähendab otsinguala suurust kolmandiku võrra. See tähendab, et Binary Search teeb vähem
    # rekursiivseid kutseid ja võrdlusi, mis muudab selle kiiremaks.

    # Üldiselt on Binary Search eelistatud valik, kuna selle aegkompleksus on väiksem ja see on praktiliselt kiirem
    # enamikes olukordades.