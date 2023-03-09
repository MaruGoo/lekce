import json
with open('person.json', encoding='utf-8') as vstupni_soubor:
    person = json.load(vstupni_soubor)

prospech_slovnik = {}
for body in person:
    if (person[body]) >= 60:
        prospech_slovnik[body] = "Pass"
    else:
        prospech_slovnik[body] = "Fail"
with open("person_prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(prospech_slovnik, vystupni_soubor, ensure_ascii=False, indent=4)

