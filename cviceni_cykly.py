# cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

# # Priklad 1
# # a)
# nasobky = []
# for cislo in cisla: 
#     nasobky.append(cislo * 2)

# print(nasobky)
# nasobky = [cislo * 2 for cislo in cisla]
# print(nasobky)

# # b)
# minusky = []
# for cislo in cisla: 
#     minusky.append(cislo * -1)

# print(minusky)

# # c)
# mocniny = []
# for cislo in cisla: 
#     mocniny.append(round(cislo ** 2, 2))

# d)


# Priklad 2
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
pocty_pismen = [len(jmeno) for jmeno in jmena]
print(pocty_pismen)

velka_pismena = [jmeno.upper() for jmeno in jmena]
print(velka_pismena)

jmena_a = [jmeno + "a" for jmeno in jmena]
print(jmena_a)

jmena_email = [(jmeno + "@email.cz").lower() for jmeno in jmena]
print(jmena_email)





