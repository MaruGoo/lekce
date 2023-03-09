a = 5
b = 10

def mult(a, b):
    return a * b

print(mult(a, b))

person_price = 850
breakfast_price = 125

#pocet_osob = int(input("Zadejte prosím počet osob: "))
#total_price = (person_price * pocet_osob)+(breakfast_price * pocet_osob)

#print(total_price)

def total_price(pocet_osob, breakfast=False):
    #return (person_price * pocet_osob)+(breakfast_price * pocet_osob)
    if breakfast:
        return (person_price * pocet_osob)+(breakfast_price * pocet_osob)
    else:
        return (person_price * pocet_osob)
print(total_price(3))
print(total_price(2, True))








