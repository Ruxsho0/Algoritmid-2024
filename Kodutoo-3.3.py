# Jump Search on otsingu algoritm, mis töötab sorteeritud massiivide peal.
# Algoritm jagab massiivi väiksemateks osadeks ja hüppab läbi massiivi kindla sammu võrra, et leida otsitav element.
# Kui hüppega leitakse vahemik, kus otsitav element võib asuda, tehakse selles vahemikus lineaarne otsing.

# Pseudo-kood:
# function jump_search(arr, target):
#     n = length(arr)
#     step = sqrt(n)
#     prev = 0
#     while arr[min(step, n) - 1] < target:
#         prev = step
#         step += sqrt(n)
#         if prev >= n:
#             return -1
#     for i from prev to min(step, n):
#         if arr[i] == target:
#             return i
#     return -1

# 2. Ajaline komplekssus
# Jump Search'i ajaline komplekssus on O(sqrt(n)), kuna hüpatakse läbi massiivi sqrt(n) sammuga ja seejärel tehakse lineaarne otsing.
# Linear Search'i ajaline komplekssus on O(n), kuna iga element tuleb läbi vaadata.
# Binary Search'i ajaline komplekssus on O(log n), kuna massiiv jagatakse iga kord pooleks.

# 3. Stsenaariumid, kus Jump Search võib olla efektiivsem
# Jump Search võib olla efektiivsem kui Linear Search, kui massiiv on väga suur ja otsitav element asub massiivi alguses.
# Jump Search võib olla eelistatud ka siis, kui andmed on sorteeritud ja Binary Search'i kasutamine pole võimalik või soovitav.

def sqrt(n):                                    # ruutjuure funktsioon
    return int(n ** 0.5)                        # tagastab täisarvu

def jump_search(arr, target):                   # Jump Search algoritm
    n = len(arr)                                # massiivi pikkus
    step = sqrt(n)                              # samm on ruutjuur massiivi pikkusest
    prev = 0                                    # eelmine samm on 0 kuna alguses pole hüpatud

    while arr[min(step, n) - 1] < target:       # kuniks hüpatakse massiivi piires ja otsitav element on suurem kui hüpatud element
        prev = step                             # eelmine samm on hüpatud samm
        step += sqrt(n)                         # sammule lisan ruutjuure massiivi pikkusest
        if prev >= n:                           # kui eelmine samm on suurem või võrdne massiivi pikkusega
            return -1                           # tagasta -1, kuna elementi ei ole massiivis, all pool muudan selle vastuseks, et ei ole massiivis

    for i in range(prev, min(step, n)):         # hüpatud sammust kuni minimaalse sammuni
        if arr[i] == target:                    # kui element massiivis on otsitav element
            return i                            # tagasta elemendi indeks

    return -1

# Test
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 144
result = jump_search(arr, target)
if result == -1:
    print(f"Element {target} ei ole massiivis")
else:
    print(f"Element {target} on massiivis indeksil {result}")