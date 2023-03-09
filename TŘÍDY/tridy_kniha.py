

# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Kniha, která reprezentuje knihu. Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.
class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena

    # Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
    def __str__(self):
        return f"Kniha se jmenuje: {self.nazev}, má: {self.pocet_stran} stran a její cena je: {self.cena} Kč"

    # Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.
    def sleva(self, vyse_slevy):
       self.cena = self.cena - (vyse_slevy * self.cena)

kniha_1 = Kniha("Dva roky prazdnin", pocet_stran=300, cena=400)
print(kniha_1)
kniha_1.sleva(vyse_slevy=0.50)
print(kniha_1)