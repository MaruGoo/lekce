# Aplikace pro zasílání SMS zpráv

def overeni_cisla(telefonni_cislo):
    if len(telefonni_cislo) ==9 or (len(telefonni_cislo)==13 and telefonni_cislo[0:4]=="+420"):
        return True
    else:
        return False

def k_zaplaceni(zprava):
    castka = (((len(zprava)//180))+1)*3
    return(castka)

telefonni_cislo = input("Zadejte telefonní číslo, na které chcete zprávu zaslat: ")
if (overeni_cisla(telefonni_cislo)) == False:
    print("Zadané číslo nemá správný formát.")
else:
    zprava = input("Napiště zprávu, kterou chcete odeslat: ")
    print(f"K zaplacení {k_zaplaceni(zprava)} Kč")
