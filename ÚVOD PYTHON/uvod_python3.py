>>> znak = 30
>>> len(nazev)
19    
>>> delka_nazvu = znak * 19
>>> delka_nazvu
570
>>>
>>> eura = 12 * 0.65
>>> round(eura)
8
>>> koruny = round(eura) * 24
>>> koruny
192
>>>
>>> import math
>>> eura = math.ceil(12 * 0.65)
>>> eura
8
>>>
>>> import random
>>> randint(1,24)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'randint' is not defined
>>> random.randint(1,24)
11
>>>
>>> random.randint(1,24)
21
>>> random.randint(1,24)
20