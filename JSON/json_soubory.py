import json
with open('api.json', encoding='utf-8') as soubor:
    lide = json.load(soubor)
print(lide)
import requests
response = requests.get('https://api.kodim.cz/python-data/people')
people = json.loads(response.text)
print(people)
print(len(people))
print(people[0])
for klic in people[0]: 
    print(klic)
for person in people:
    print(person)

zeny = []
muzi = []
for person in people:
    pohlavi = person["gender"]
    if pohlavi == 'Female':
        zeny.append(person)
    else:
        muzi.append(person)

print(f"Pocet muzu: {len(muzi)}")
print(f'Pocet zen: {len(zeny)}')







