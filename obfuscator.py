import random
import datetime
import os

file = open(os.environ["HOMEPATH"] + "\Desktop\output.py", 'w')

s = """
print(' '.join(list('obfuscation')))
"""

# 0-10 ranges
FALSE_VARIATION = 10 # amount of n-0 (fake math) to be generated on the code
PIPED_VARIATION = 10 # amount of bitwise xor stuff to be generated on the code

DEBUG = False

obf=[]
obfieds=[]

# Test each chr (n(O)) to be checked until you get the right thing
for e in s:
    for i in range(10000):
        if chr(i) == e:
            obf.append(i)

print('Char Table =', obf)

# Main system
for i in obf:
    build = ''
    chance = 90

    if DEBUG: print(f'>>> Obfuscating char {i}')

    # Inside the while loop we use [:-1] because the last symbol isnt recognized (+ or -)
    while True:
        rng = random.randrange(100) >= chance
        if rng: 
            build += 'True+'

            # Settings usage
            if random.randrange(11)<PIPED_VARIATION: build += random.choice(['(not False|False|True|False|True)+', '((True ^ False | 128 | 256 | 1024 | 2048 | 4096)-0x1d81)+'])
            if random.randrange(11)<FALSE_VARIATION: build += 'False+'

        else: 
            build+='True-'
            # Settings usage
            if random.randrange(11)<PIPED_VARIATION: build += random.choice(['(len(str(KeyError)*0x3)-0x36)-', '((1|0x128*512*1024|128&(1^2^4^8^16^32^64^128^256^512^1024^2048))-0x128*512*1024-0xf-0xf-0xf-0xf-69)-'])
            if random.randrange(11)<FALSE_VARIATION: build += 'False-'

        # Chance system
        # Flutuates depending of how far is the built TrueFalse string length, greater -> chance to subtract it is higher
        if eval(build[:-1])>i: chance += 5
        else: chance -= 5

        if eval(build[:-1])==i:
            obfieds.append(build[:-1])
            if DEBUG: print(f'>> Successfully obfuscated {i}, total length is now {len(obfieds[-1])}')
            break 
        # print(rng)
else:
    print(f'\n>>> Finished Obfuscating {len(obf)} characters! <<<')


# Obfuscated code variables
li = 'lI'
gen = ''
separator = 'nothing_to_see_here'
sep=''
index=''

AGGRESSIVENESS = {
    'Variable Size':64, # length of the lilililililili variable
    'Separator Size':128, # length of each character separation
    'Index Size':8192 # length of the i (for i) variable name
}

print(f'>>> Writing the obfuscated code to file {file.name}')

# High values = more time to obfuscate but harder to understand the code.
for i in range(AGGRESSIVENESS['Variable Size']): gen+=random.choice(list(li))
for i in range(AGGRESSIVENESS['Separator Size']): sep+=random.choice(list(separator))
for i in range(AGGRESSIVENESS['Index Size']): index+=random.choice(list(separator))

# troll
output = f'# synthetic $ field {hex(len(f"{sep}".join(obfieds)))}\n{gen}=\"{f"{sep}".join(obfieds)}\"\n{gen[::-1]}=""\nfor {index} in {gen}.split("{sep}"): {gen[::-1]}+=chr(eval({index}))\nexec({gen[::-1]})\n\n# Auto-Generated\n# {datetime.datetime.now()}'

raw = [chr(eval(i)) for i in obfieds]

print(f'{"-"*30}\nReal (compiled) code:\n'+''.join(raw).strip())
#print(output)

# Copy to clipboard
file.write(output)
print(f'\n>>> Successfully wrote {len(output)} characters of code to {file.name}!')
file.close()

print(f'{"-"*30}\nPython 3.11.0 Compiled: \n')
exec(output)
print('-'*30)
