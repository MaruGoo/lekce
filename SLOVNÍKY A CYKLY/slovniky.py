# Pekarna ma polozky a ceny v korunach
pekarna = {
    "houska": 10, 
    "kolac": 15, 
    "chleba": 40, 
    "muffin": 20,
    "loupak": 20,
    "frgal": 50
}

print(pekarna["kolac"]) #vypise hodnotu pro klic kolac

klic = "frgal"
print(f'klic: {klic}, hodnota: {pekarna[klic]}') 
print('klic: ' + klic + ', hodnota: ' + str(pekarna[klic]))

produkt = input("Zadej produkt: ")

if produkt in pekarna:  # Produkt je v pekarne = klic je ve slovniku (klic je jeden z klicu)
    print(f'{produkt} stoji {pekarna[produkt]} korun.')
else:  # Produkt neni v pekarne = klic neni ve slovniku
    print(f'Bohuzel, produkt {produkt} neprodavame.')

nove_produkty = {"zavin": 150, "buchta": 150}
pekarna.update(nove_produkty)  # Upravi slovnik pekarna a prida nove_produkty
print(pekarna)