# Zaměstnanec: jmeno, pozice
frantisek = ["Frantisek Novak", "ucetni"]
alena = ["Alena Novotna", "sefova"]

zamestnanec = ["Frantisek Novak", "ucetni"]
frantisek = {"jmeno": "Frantisek Novak", "pozice": "ucetni"}
frantisek = ["jmeno" = "Frantisek Novy"]
alena = {"jmeno": "Alena Novotna", "pozice": "sefova"}

class Zamestnanec:  # definice tridy
    jmeno = ""  # atribut tridy
    pozice = ""

frantisek = Zamestnanec()  # objekt
frantisek.jmeno = "Frantisek Novak"
frantisek.pozice = "ucetni"

print(frantisek.jmeno)
print(frantisek.pozice)

class Zamestnanec:  # definice tridy
    def __init__(self, jmeno, pozice):  # konstruktor tridy - specialni metoda
        self.jmeno = jmeno  # atribut tridy
        self.pozice = pozice

    def __str__(self):  # urcuje, jaky bude vysledek volani funkce str() na objekty tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def info(self):  # metoda tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    print(info)