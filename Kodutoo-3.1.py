def linear_search(arr, target):                     # kui element on massiivi lõpus, siis on vaja kõik elemendid üle vaadata
    for index, value in enumerate(arr):             # kui element on massiivi alguses, siis on vaja ainult 1 elementi üle vaadata
        if value == target:                         # kui element on massiivi keskel, siis on vaja vähemalt n/2 elementi üle vaadata
            return index                            # kui elementi ei ole massiivis, siis on vaja kõik elemendid üle vaadata
    return -1                                       # kui element on massiivis, siis on vaja ainult 1 elementi üle vaadata

arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)

if result != -1:
    print(f"Element leiti {result} kohalt")
else:
    print("Elementi ei leitud")

# Selle algoritmi ajaline keerukus on O(n), sest kui element on massiivi lõpus, siis on vaja kõik elemendid üle vaadata, mida suurem on massiiv seda kauem aega võtab.
# Linear Searchi saab reaalmaailmas näiteks raamatukogus raamatu leidmiseks. Kuid mida rohkem raamatuid on seda raskemaks see läheb.
# Linear Search võtab väga kaua aega kuna on vaja kõik elemendid üle vaadata.