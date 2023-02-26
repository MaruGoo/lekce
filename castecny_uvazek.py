class Zamestnanec:  # definice tridy
    def __init__(self, jmeno, pozice):  # konstruktor tridy - specialni metoda
        self.jmeno = jmeno  # atribut tridy
        self.pozice = pozice

    def __str__(self):  # urcuje, jaky bude vysledek volani funkce str() na objekty tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

    def info(self):  # metoda tridy
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, uvazek):
        super().__init__(jmeno, pozice="Brigadnik")
        self.jmeno = jmeno
        self.uvazek = uvazek
    def __str__(self):
        return f"Brigadnik {self.jmeno} pracuje na uvazek: {self.uvazek}"

alena = Brigadnik(jmeno="Alena", uvazek="plný")
print(alena)
