# Aplikace pro zasílání SMS zpráv

telefonni_cislo = input("Zadejte telefonní číslo, na které chcete zprávu zaslat: ")
delka_cisla = len(telefonni_cislo)
print(delka_cisla)

if delka_cisla == 13:
    if telefonni_cislo[0:3] == +420:
        zprava = input("Napiště zprávu, kterou chcete odeslat: ")
    else:
        print("Zadali jste nesprávnou předvolbu")
elif delka_cisla == 9:
    zprava = input("Napiště zprávu, kterou chcete odeslat: ")
else: 
    print("zadané číslo nesplňuje požadavky (počet znaků musí být 9 nebo 13 s předvolbou)")
    exit()
    print("Zadali jste nesprávnou předvolbu")

print(f"K zaplacení {((len(zprava)//180))+1*3} Kč")