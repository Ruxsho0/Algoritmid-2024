def insertion_sort(arr):                                # Lisamise sorteerimise algoritm
    for i in range(1, len(arr)):                        # Välimine tsükkel, mis kordub n korda
        key = arr[i]                                    # Määrame key väärtuseks i
        j = i - 1                                       # Määrame j väärtuseks i-1
        while j >= 0 and key < arr[j]:                  # Tsükkel, mis kordub n-i-1 korda
            arr[j + 1] = arr[j]                         # Vahetame elemendid omavahel
            j -= 1                                      # Vähendame j väärtust ühe võrra
        arr[j + 1] = key                                # Määrame arr[j+1] väärtuseks key
        print(f"{i}: {arr}")                            # Prindib massiivi pärast iga läbimist
    return arr



array = [12, 11, 13, 5, 6, 7]                           # Kodutöö 2.3 massiiv
print("Originaal:", array)                              # Prindib algse massiivi
sorted_array = insertion_sort(array)                    # Kutsub välja lisamise sorteerimise funktsiooni
print("Sorteeritult:", sorted_array)                    # Prindib sorteeritud massiivi

# [12, 11, 13, 5, 6, 7] -> [11, 12, 13, 5, 6, 7] -> [11, 12, 13, 5, 6, 7] -> [5, 11, 12, 13, 6, 7] -> [5, 6, 11, 12, 13, 7] -> [5, 6, 7, 11, 12, 13]

# Insertion sort ei ole kasulik suurte massiivide puhul, kuna selle aja keerukus on O(n^2). Kui massiiv on juba sorteeritud, siis on selle aja keerukus O(n).
# Insertion sort on kasulik väikeste massiivide puhul, kuna selle aja keerukus on O(n^2). Kui massiiv on juba sorteeritud, siis on selle aja keerukus O(n).
# Insertion sort on selle massiivi puhul kasulik, kuna massiiv on väike ja sorteerimiseks kulub vähem aega.
# Sammuti on see massiiv juba pooleldi sorteeritud.