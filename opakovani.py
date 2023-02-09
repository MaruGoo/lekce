print("Vítejte u nas v divadle!") # retězec, string, str

nazev_hry = "Romeo a Julie"

cena_listku = 150
pocet_listku = int(input("Zadejte prosím počet listku: "))

celkova_cena = cena_listku * pocet_listku

# Pokud je pocet listku alespon 3, dostane zakaznik slevu 10%
if pocet_listku >=3:
    zlevnena_cena = celkova_cena * 0.90
    print(f"Celkova cena listku na predstaveni {nazev_hry} je {zlevnena_cena}. Usetrili jste 10% oproti puvodni cene {celkova_cena}")
else:
    print(f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}.")

