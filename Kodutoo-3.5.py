# Konkreetse faili või kausta leidmine arvutis.

# Selle stsenaariumi jaoks sobib kõige paremini binaarne otsing, kui failid on sorteeritud.

# Näide binaarse otsingu rakendamisest Pythonis:

def binary_search(file_list, target):
    left, right = 0, len(file_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if file_list[mid] == target:
            return mid
        elif file_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Näidisandmed (sortitud failide nimekiri)
files = ["document.txt", "image.png", "music.mp3", "video.mp4"]

# Otsime konkreetset faili
target_file = "music.mp3"
result = binary_search(files, target_file)

if result != -1:
    print(f"Fail '{target_file}' leiti indeksil {result}.")
else:
    print(f"Faili '{target_file}' ei leitud.")

# Potentsiaalsed modifikatsioonid:
# 1. Kui failide nimekiri ei ole sorteeritud, tuleks see enne otsingut sorteerida.
# 2. Kui failide nimekiri muutub sageli, võib kasutada andmestruktuuri, mis toetab kiiret lisamist ja otsingut, näiteks tasakaalustatud binaarpuud (AVL või punane-must puu).
# 3. Kui failide nimekiri on väga suur, võib kaaluda HASH TABLE kasutamist, mis pakuvad keskmiselt O(1) otsinguaega.

# Näiteks windows 11 otsib faile ja kaustu, kui sisestada otsinguribale mingi sõna, siis otsib windows 11 selle sõna järgi faile ja kaustu.
# Windows kasutab algoritmi sarnast binaarse otsinguga, kuna failid ja kaustad on sorteeritud ja otsing on kiirem.