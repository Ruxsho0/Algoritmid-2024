def bubble_sort(arr):                                       # Bublesort sorteerimise algoritm
    n = len(arr)                                            # Määrame massiivi pikkuse
    for i in range(n):                                      # Välimine tsükkel, mis kordub n korda
        for j in range(0, n-i-1):                           # Sisemine tsükkel, mis kordub n-i-1 korda
            if arr[j] > arr[j+1]:                           # Kui praegune element on suurem kui järgmine element
                arr[j], arr[j+1] = arr[j+1], arr[j]         # Vahetame elemendid omavahel
        print(f"{i+1}: {arr}")                              # Prindib massiivi pärast iga läbimist
    return arr                                              # Tagastame sorteeritud massiivi

arr = [64, 34, 25, 12, 22, 11, 90]                          # Kodutöö 2.1 massiiv
sorted_arr = bubble_sort(arr)                               # Kutsub välja mulli sorteerimise funktsiooni
print("Sorteeritult:", sorted_arr)                          # Prindib sorteeritud massiivi