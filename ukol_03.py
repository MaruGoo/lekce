import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
print(body)

for person in body:
    print(f"klic je {person} a jeho hodnota je {body[person]}")
    if body >=60:
        print(f"Pass")
    else:
        print(f"Fail")

