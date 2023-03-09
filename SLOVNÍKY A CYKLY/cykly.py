# jmena = ["Anna", "Adela", "Alena", "Adam"]

# for jmeno in jmena: 
#     print(jmeno)

pocet_hracu = 4
# import random
# hod_1 = random.randint(1, 6)
# hod_2 = random.randint(1, 6)
# hod_3 = random.randint(1, 6)
# hod_4 = random.randint(1, 6)
# # chceme tolikrat hodit kostkou, kolik mame hracu
# print(hod_1, hod_2, hod_3, hod_4)

# print(list(range(pocet_hracu)))
import random

for hrac in range(pocet_hracu):
    print(f"Hrac {hrac} hodil {random.randint(1, 6)}.")