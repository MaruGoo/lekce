
class Balik:
    def __init__(self, adresa, hmotnost):  # konstruktor tridy - specialni metoda
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
    def doruc(self):
        self.doruceno = True
    def __str__(self):
        return f"Adresa: {self.adresa}, hmotnost balíku: {self.hmotnost}, stav balíku: {self.doruceno}"

Balik_1 = Balik("Na Příkopech 12", "1300 g")
# Balik_1.adresa = "Na Příkopech 12"
# Balik_1.hmotnost = "1300 g"

# print(Balik_1.adresa)
# print(Balik_1.hmotnost)
print(Balik_1)
Balik_1.doruc()
print(Balik_1)
