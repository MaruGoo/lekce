import pandas

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
# print(staty)

print(staty.loc["Andorra"])
print(staty.loc[["Andorra", "Slovakia"]])
print(staty.loc[["Andorra", "Slovakia"], ["region", "gini"]])  # .loc[radky, sloupce]

staty = staty.set_index("alpha3Code")
print(staty.loc["AND"])
print(staty.index)

staty = staty.reset_index() # vrátím změny v indexu zpět na původní
print(staty)

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

print(staty["area"])
# Vrati Series s hodnotami True/False, pokud (ne)splnuji podminku
print(staty["area"] < 1000)

# Vyfiltruj tabulku staty (vrat radky, kde je hodnota True)
print(staty[staty["population"] > 200_000_000])

# Staty, kterych hl.mesto zacina na pismeno
pismeno = "B"
print(staty[staty["capital"].str.startswith(pismeno)])

lidnate_staty = staty[staty["population"] > 200_000_000]
print(lidnate_staty[["capital", "region", "gini"]])

# Staty, ktere jsou v regionu Evropa:
# print(staty["region"] == "Europe")
print(staty[staty["region"] == "Europe"])

# Staty, ktere jsou v regionu Evropa NEBO Asie:
print(staty[(staty["region"] == "Asia") | (staty["region"] == "Europe")])