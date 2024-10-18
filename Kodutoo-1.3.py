def fibonacci(n):
    if n <= 0: # kontrollib, kas sisend on positiivne täisarv
        return "Sisend peab olema positiivne täisarv."
    elif n == 1: # kui n on 1, tagastab Fibonacci jada esimese liikme
        return [0]
    elif n == 2: # kui n on 2, tagastab Fibonacci jada esimesed kaks liiget
        return [0, 1]
    else:
        fib_jada = [0, 1] # loob listi, kuhu salvestatakse Fibonacci jada
        for i in range(2, n): # arvutab Fibonacci jada n esimest liiget
            järgmine_number = fib_jada[-1] + fib_jada[-2] # leiab järgmise Fibonacci jada liikme
            fib_jada.append(järgmine_number) # lisab järgmise Fibonacci jada liikme listi
        return fib_jada # tagastab Fibonacci jada

# Näide kasutamisest:
n = 10
print(f"Esimesed {n} numbrit Fibonacci jadas: {fibonacci(n)}")

# Rekursioon on tehnika kus funktsioon kutsub iseennast. Ta kutsub ennast nii kaua kuniks jouab kas n = 0 voi n = 1. 
# Ajaline keerukus sellel on O(2^n), sest iga kord kui funktsioon kutsub ennast, kutsub ta ennast uuesti kaks korda.
# See ei ole kõige parem suuremate andemetega, sest see võtab väga palju aega.