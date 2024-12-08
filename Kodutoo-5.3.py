"""
- Binaarne otsingupuu (BST) on andmestruktuur, kus igal sõlmel on maksimaalselt kaks last: vasak ja parem.
- Iga sõlme vasak alampuu sisaldab ainult väärtusi, mis on väiksemad kui sõlme enda väärtus.
- Iga sõlme parem alampuu sisaldab ainult väärtusi, mis on suuremad kui sõlme enda väärtus.
- BST põhielemendid on sõlmed, mis koosnevad väärtusest, viitest vasakule lapsele ja viitest paremale lapsele.
- Tasakaalustamata puud võivad põhjustada halvimat juhtumit, kus puu muutub sarnaseks lingitud loendiga, mille tulemusena otsingu,
lisamise ja kustutamise operatsioonide ajakeerukus muutub O(n).
- Tasakaalustamata puude tõhusust saab optimeerida, kasutades tasakaalustamise meetodeid nagu AVL puud või punane-must puud,
tagades operatsioonide keskmise ajakeerukuse O(log n).
"""