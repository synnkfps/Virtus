import random

s = """
for e in s:
    for i in range(10000):
        if chr(i) == e:
            obf.append(i)
"""

obf=[]
obfieds=[]

for e in s:
    for i in range(10000):
        if chr(i) == e:
            obf.append(i)

print(obf)


booleans = [True, False]
ops = ['+', '-']

for i in obf:
    build = ''
    chance = 90

    while True:
        rng = random.randrange(100)>=chance
        if rng: build+='True+'
        else: build+='True-'

        if eval(build[:-1])>i: chance += 5
        else: chance -= 5

        if eval(build[:-1])==i:
            obfieds.append(build[:-1])
            break 
        # print(rng)

print(obfieds)

raw = ''
for i in obfieds:
    raw+=chr(eval(i))

print(raw)
