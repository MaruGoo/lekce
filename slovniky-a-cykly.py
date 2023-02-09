sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Pri prochazeni pres slovnik prochazime pres jeho klice
for kniha in sales:  
    print(kniha)

for nazev in sales:  
    print(f'Knihy s nazvem {nazev} se prodalo {sales[nazev]} ks.')

# Jake jsou klice slovniku?
print(sales.keys())

# Jake jsou hodnoty slovniku?
print(sales.values())
# Kolik se prumerne prodalo vytisku na knihu?
print(sum(sales.values()) / len(sales))

for nazev, prodano in sales.items():  # Dvojice klic, hodnota
    print(f'Knihy s nazvem {nazev} se prodalo {prodano} ks.')