class Auto:  # definice tridy
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True
    def pujc_auto(self):
        self.pujc_auto = "Dostupne"
        if:
            self.pujc_auto = "Dostupne"
            return f"Potvrzuji zapůjčení vozidla"
        else:
            return f"Vozidlo není k dispozici"
    def get_info(self):
        return f"Vozidlo s registrační zančkou {self.registracni_znacka} {self.typ_vozidla} má najeto {self.najete_km}"


auto_1 = Auto(registracni_znacka="4A2 3020", typ_vozidla="Peugeot 403 Cabrio", najete_km=47534)
auto_2 = Auto(registracni_znacka="1P3 4747", typ_vozidla="Škoda Octavia", najete_km=41253)
print(Auto)