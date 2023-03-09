print("Ahoj")

round(12.5465, 2) #zaokrouhleni na 2 des. mista

a = 8
b = 5
print(a + b)

def secti(a, b):    #paramentry
    #print(a + b)
    return a + b

vysledek = secti(8, 5)  #argumenty

print(f"Vysledek je: {vysledek}")   #ukladam si promennou vysledek pro dalsi pouziti

# Ke kazdemu cislu v seznamu pricti 1 pomoci funkce "secti"
seznam_cisel = [2, 5, 9, 8]

# Vysledek jen vypiseme
for cislo in seznam_cisel:
    print(secti(cislo, 1))

# Vysledky ulozime do noveho seznamu
soucty = []
for cislo in seznam_cisel:
    soucty.append(secti(cislo, 1))

print(soucty)