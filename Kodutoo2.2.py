def selection_sort(arr):                                                # Valiku sorteerimise algoritm
    n = len(arr)                                                        # Määrame massiivi pikkuse
    for i in range(n):                                                  # Välimine tsükkel, mis kordub n korda
        min_idx = i                                                     # Määrame min_idx väärtuseks i
        for j in range(i+1, n):                                         # Sisemine tsükkel, mis kordub n-i-1 korda
            if arr[j] < arr[min_idx]:                                   # Kui praegune element on väiksem kui min_idx element
                min_idx = j                                             # Määrame min_idx väärtuseks j
        print(f"{i+1} - V2ikseim element on: {arr[min_idx]}")           # Prindime väikseima elemendi
        arr[i], arr[min_idx] = arr[min_idx], arr[i]                     # Vahetame elemendid omavahel
    return arr                                                          # Tagastame sorteeritud massiivi

arr = [29, 15, 56, 77, 18]                                              # Kodutöö 2.2 massiiv
sorted_arr = selection_sort(arr)                                        # Kutsub välja valiku sorteerimise funktsiooni
print("Sorteeritult:", sorted_arr)                                      # Prindib sorteeritud massiivi