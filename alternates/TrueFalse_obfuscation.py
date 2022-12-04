import random
import datetime
import subprocess
import os

file = open(os.environ["HOMEPATH"] + "\Desktop\output.txt", 'w')

s = """
for i in 'obfuscation': print(i)
"""

# 0-10 ranges
FALSE_VARIATION = 10 # amount of n-0 (fake math) to be generated on the code
PIPED_VARIATION = 10 # amount of bitwise xor stuff to be generated on the code

obf=[]
obfieds=[]

# Test each chr (n(O)) to be checked until you get the right thing
for e in s:
    for i in range(10000):
        if chr(i) == e:
            obf.append(i)

print('Char Table', obf)

# 1,0,+,-
booleans = [True, False]
ops = ['+', '-']

# Main system
for i in obf:
    build = ''
    chance = 90

    # Inside the while loop we use [:-1] because the last symbol isnt recognized (+ or -)
    while True:
        rng = random.randrange(100)>=chance
        if rng: 
            build+='True+'

            # Settings usage
            if random.randrange(11)<PIPED_VARIATION: build+= random.choice(['(not False|False|True|False|True)+', '((True ^ False | 128 | 256 | 1024 | 2048 | 4096)-0x1d81)+'])
            if random.randrange(11)<FALSE_VARIATION: build+='False+'

        else: 
            build+='True-'
            # Settings usage
            if random.randrange(11)<PIPED_VARIATION: build+='(len(str(KeyError)*0x3)-0x36)-'
            if random.randrange(11)<FALSE_VARIATION: build+='False-'

        # Chance system
        # Flutuates depending of how far is the built TrueFalse string length, greater -> chance to subtract it is higher
        if eval(build[:-1])>i: chance += 5
        else: chance -= 5

        if eval(build[:-1])==i:
            obfieds.append(build[:-1])
            break 
        # print(rng)

li = 'lI'
gen = ''
separator = 'nothing_to_see_here'
sep=''
index=''

for i in range(64): gen+=random.choice(list(li))
for i in range(128): sep+=random.choice(list(separator))
for i in range(8192): index+=random.choice(list(separator))

# troll
output = f'# synthetic $ field {hex(len(gen))}\n{gen}=\"{f"{sep}".join(obfieds)}\"\n{gen[::-1]}=""\nfor {index} in {gen}.split("{sep}"): {gen[::-1]}+=chr(eval({index}))\nexec({gen[::-1]})\n\n# Auto-Generated\n# {datetime.datetime.now()}'

print(f'{"-"*30}\n Generated variable string:',gen)

raw = [chr(eval(i)) for i in obfieds]

print(f'{"-"*30}\nReal (compiled) code:\n'+''.join(raw).strip())
#print(output)

# Copy to clipboard
file.write(output)
print(f'Saved to {file}!')
file.close()

print(f'{"-"*30}\nPython 3.11 Compiled: \n')
exec(output)
print('-'*30)
