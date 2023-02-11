import pandas

jmena = pandas.read_csv("jmena.csv")
# print(jmena)

jmena = jmena.set_index("jméno") 

# Vypište na konzoli informace o jménu Jiří.
print(jmena.loc["Jiří"]) #a

# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(jmena.loc[["Martin", "Zuzana", "Josef"]]) #b

# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(jmena[jmena["četnost"] > 188_000]) #c
print(jmena.iloc [0:8]) #c
print(jmena.loc["Jiří":"Martin"]) #c

# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(jmena.loc["Martin":"Tereza","věk"]) #d

# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(jmena[["věk","původ"]].loc["Libor": ]) #e

# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print(jmena.loc[:,"věk":"původ"]) #f

# Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
bool_index = jmena["věk"] > 60
print(bool_index)

data_60 = jmena[bool_index]
print(data_60)

# Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
bool_index = (jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)
print(bool_index)

data_cetnost = jmena[bool_index]
print(data_cetnost)

# Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je
