class Zamestnanec:  # definice tridy
    def __init__(self, jmeno, pozice):  # konstruktor tridy - specialni metoda
        self.jmeno = jmeno  # atribut tridy
        self.pozice = pozice

    def __str__(self):  # urcuje, jaky bude vysledek volani funkce str() na objekty tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def info(self):  # metoda tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

frantisek = Zamestnanec (jmeno="Frantisek Novak", pozice="ucetni")
print(frantisek)

class Manazer(Zamestnanec): # Manazer dedi od Zamestnance - Manazer prebira atributy a metody Zamest.
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_podrizenych = pocet_podrizenych

class Manazer(Zamestnanec): # Manazer dedi od Zamestnance - Manazer prebira atributy a metody Zamest.
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        super().__init__(jmeno, pozice)
        self.pocet_podrizenych = pocet_podrizenych
    def __str__(self):
        return f"{super().__str__()} a ma tym o velikosti {self.pocet_podrizenych}."

alena = Manazer(jmeno="Alena", pozice="Sefova vsech ucetnich", pocet_podrizenych=3)
print(alena.jmeno)
print(alena.pozice)
print(alena.pocet_podrizenych)

class Manazer(Zamestnanec):
    def __init__(self, jmeno, pocet_podrizenych):
        super().__init__(jmeno, pozice="manazer")
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return f"{super().__str__()} a ma tym o velikosti {self.pocet_podrizenych}."
    
    def info(self):
        return f"{super().info()} a ma tym o velikosti {self.pocet_podrizenych}."

alena = Manazer("Alena Novotna", pocet_podrizenych=3)
print(alena)

andrea = Manazer("Andrea Nova", pocet_podrizenych=10)
print(andrea)