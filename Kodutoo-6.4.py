# Bellman-Fordi Algoritmi Teoreetiline Analüüs

# Bellman-Fordi Algoritmi Kirjeldus:
# Bellman-Fordi algoritmi kasutatakse lühimate teede leidmiseks ühest alguspunktist kõigi teiste tippudeni kaalutud graafis.
# Erinevalt Dijkstra algoritmist, mis töötab ainult mitte-negatiivsete kaaludega graafide puhul, suudab Bellman-Ford käsitleda ka negatiivsete kaaludega graafe.

# Erinevused Bellman-Fordi ja Dijkstra Algoritmi vahel:
# 1. Bellman-Ford suudab käsitleda negatiivseid kaale, samas kui Dijkstra algoritm ei suuda.
# 2. Bellman-Fordi algoritmi ajakeerukus on O(V * E), kus V on tippude arv ja E on servade arv.
#    Dijkstra algoritmi ajakeerukus on O(V^2) või O(E + V log V) prioriteedijärjekorraga.
# 3. Bellman-Ford suudab tuvastada negatiivse kaaluga tsükleid, samas kui Dijkstra algoritm ei suuda.

# Negatiivsete Tsüklite Tuvastamine:
# Bellman-Fordi algoritm suudab tuvastada negatiivse kaaluga tsükleid, tehes ühe lisaiteratsiooni kõigi servade üle pärast V-1 iteratsiooni.
# Kui mõnda serva saab endiselt lõdvendada, näitab see negatiivse kaaluga tsükli olemasolu.

# Negatiivsete Tsüklite Tuvastamise Praktiline Tähtsus:
# Negatiivse kaaluga tsüklite tuvastamine on oluline erinevates rakendustes, nagu finantsarbitraaž, võrgu marsruutimine ja piirangute rahuldamise probleemid.
# Negatiivsed tsüklid võivad viia arbitraaživõimalusteni valuutavahetuses või näidata vastuolusid piirangute kogumis.