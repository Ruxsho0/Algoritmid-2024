# Fibonacci Search algoritm on veel kiirem kui Binary Search,
# sest ta on keerukusega O(Log n). 

# Fibonacci Search on efektiivne suurte sorteeritud massiivide puhul,
# kuna see vähendab otsinguruumi kiiremini kui lineaarne otsing ja võib olla efektiivsem kui binaarne otsing,
# kui mälu ligipääs on kallis.
# Fibonacci numbrite kasutamine võimaldab algoritmil jagada massiivi osadeks viisil, mis võib vähendada mälu ligipääsu operatsioonide arvu.

# Fibonacci Search algoritm oleks parem kui Binary Search, näiteks kui massiivis on palju korduvaid element ja 
def fibonacci_search(arr, target):
    n = len(arr)
    fib2 = 0  
    fib1 = 1  
    fibM = fib2 + fib1

    while (fibM < n):
        fib2 = fib1
        fib1 = fibM
        fibM = fib2 + fib1

    offset = -1

    while (fibM > 1):
        i = min(offset + fib2, n-1)

        if (arr[i] < target):
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif (arr[i] > target):
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i

    if(fib1 and arr[offset + 1] == target):
        return offset + 1

    return -1

# Fibonacci Search on O(Log n) keerukusega, mis on kiirem kui Linear Search
arr = [10, 10, 22, 22, 35, 40, 45, 50, 80, 80, 82, 85, 90, 100]
target = 80
result = fibonacci_search(arr, target)
if result == -1:
    print("Elementi ei leitud massiivist.")
else:
    print("Element on massiivi indeksil:", result)

    # Antud massiivis on Fibonacci Search kiirem kui Binary Search
    # kuna massiivis on palju korduvaid elemente ja ta leiab need kiiremini kui Binary Search.
    
        