def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

    # igal korral on vaja läbi vaadata log n elementi, kus n on massiivi pikkus

def linear_search(arr, target):                     # kui element on massiivi lõpus, siis on vaja kõik elemendid üle vaadata
    for index, value in enumerate(arr):             # kui element on massiivi alguses, siis on vaja ainult 1 elementi üle vaadata
        if value == target:                         # kui element on massiivi keskel, siis on vaja vähemalt n/2 elementi üle vaadata
            return index                            # kui elementi ei ole massiivis, siis on vaja kõik elemendid üle vaadata
    return -1                                       # kui element on massiivis, siis on vaja ainult 1 elementi üle vaadata

def example_scenario():                             # kasutus
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    print(f"Array: {arr}")
    print(f"Target: {target}")

    binary_result = binary_search(arr, target)
    linear_result = linear_search(arr, target)

    print(f"Binary Search tulemus: Index {binary_result}")
    print(f"Linear Search tulemus: Index {linear_result}")

# Binary Search on kiirem kui Linear Search, kuna Binary Search on O(log n) keerukusega, samas kui Linear Search on O(n) keerukusega.
# Suurte andmestike korral on Binary Search märkimisväärselt kiirem.

if __name__ == "__main__":
    example_scenario()                        # näite funktsiooni käivitamine