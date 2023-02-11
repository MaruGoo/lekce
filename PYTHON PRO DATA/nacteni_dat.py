import pandas

nakupy = pandas.read_csv("nakupy.csv")
print(nakupy)
print(nakupy.info())
print(nakupy.shape)  # (11, 4) : (pocet_radek, pocet_sloupcu)
print(len(nakupy))  # 11 : pocet radek
print(nakupy.columns)  # sloupce tabulky
print(nakupy.head())  # Vypise prvnich 5 radku
print(nakupy.tail())  # Vypise poslednich 5 radku
print(nakupy["jmeno"])  # vyber sloupce

print(type(nakupy))  # DataFrame
print(type(nakupy["jmeno"]))  # Series (1 sloupec, 1 radek, 1 rozmer)
print(nakupy["jmeno"])  # vyber jednoho sloupce -> Series
print(nakupy[["jmeno", "vec"]])  # vyber vice sloupcu -> DataFrame
print(nakupy[["jmeno"]])  # DataFrame
print(list(nakupy["jmeno"]))  # prevod na klasicky seznam
# Vyber radek
print(nakupy.iloc[2])
print(nakupy.iloc[5])

# print(nakup.iloc[od:do+1])
print(nakupy.iloc[2:6])  # Rozsah radek od indexu 2 do indexu 5
print(nakupy.iloc[6:])  # Rozsah radek od indexu 6 do konce tabulky
# Vyber radku i sloupcu pomoci iloc
# print(nakupy.iloc[radky,sloupce])
print(nakupy.iloc[[0, 2, 6], 1])

print(nakupy.iloc[2:6, 1:3])
# Vyber radku i sloupcu - kombinace iloc a nazvu sloupcu
print(nakupy[["datum", "cena"]].iloc[2:6])