def eur_to_czk(pocet_eur):
    """
    Funkce na prevod eur do korun.
    Bere jeden parametr - pocet eur. Kurz je fixni 25kc za 1 euro.
    Vrati kolik stoji eura v korunach.
    """
    kurz = 25  # lokalni promenna - neni videt mimo telo funkce
    pocet_czk = pocet_eur * kurz
    return pocet_czk  # return pocet_eur * kurz

eura_uzivatel = int(input("Kolik si prejete smenit euro? "))
print(eur_to_czk(eura_uzivatel))

def eur_to_czk(pocet_eur, kurz=25):
    """
    Funkce na prevod eur do korun.
    Bere dva parametry - pocet eur a kurz, ktery je zakladne nastaveny na 25kc.
    Vrati kolik stoji eura v korunach.
    """
    pocet_czk = pocet_eur * kurz
    return pocet_czk


eura_uzivatel = int(input("Kolik si prejete smenit euro? "))
print(eur_to_czk(eura_uzivatel))  # kurz bude 25
print(eur_to_czk(eura_uzivatel, 28))  # prepiseme zakladni (defaultni) hodnotu kurzu

print(eur_to_czk(pocet_eur=eura_uzivatel, kurz=28))
print(eur_to_czk(kurz=28, pocet_eur=eura_uzivatel))  # Nemusi byt v poradi

print(eur_to_czk(pocet_eur=eura_uzivatel, 28))  # Bacha, nefunguje
print(eur_to_czk(eura_uzivatel, kurz=28))  # OKs