# Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
# Vytvořte seznam průměrných teplot pro každý den.

teploty_dny = []
for den in range(7):
    teploty_dny.append(f"Den {den + 1} = {teploty[den]}")
print(teploty_dny)

# Vytvořte seznam ranních teplot.

teploty_rano = [rano[0] for rano in teploty]
print(teploty_rano)

# Vytvořte seznam nočních teplot.

teploty_noc = [noc[3] for noc in teploty]
print(teploty_noc)

# Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
teploty_poledne = [poledne[1] for poledne in teploty]

teploty_poledne_noc = []
for poledne_noc in teploty:
    teploty_poledne_noc
print(teploty_poledne_noc)