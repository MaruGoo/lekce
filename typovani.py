def eur_to_czk(pocet_eur: int, kurz: int = 25)-> int:
    # typování = int => tím definuji, že výstup bude celé číslo a níže už nemusím
    # """
    # Funkce na prevod eur do korun.
    # Bere dva parametry - pocet eur a kurz, ktery je zakladne nastaveny na 25kc.
    # Vrati kolik stoji eura v korunach.
    # """
    pocet_czk = pocet_eur * kurz
    return pocet_czk

# pocet_eur = int(input("Kolik si přejete Eur: ")) tak by to vypadalo, kdybych nahoře nedefinovala int u pocet_eur
pocet_eur = input("Kolik si přejete Eur: ")

print(eur_to_czk(pocet_eur))
