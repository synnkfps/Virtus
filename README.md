# Virtus
Powerful Python Obfuscator, capable of obfuscate (only) single Python files, using a new obfuscation algorithm.

## Examples
![image](https://user-images.githubusercontent.com/93355393/234700111-cd269c85-f0c8-4706-8771-b3c048524811.png)<br>
turns into<br>
![image](https://user-images.githubusercontent.com/93355393/234700188-e0adb28e-f874-495c-99aa-97d3465db4d6.png)

Obfuscating settings/output: <br>
![image](https://user-images.githubusercontent.com/93355393/234700299-45f38bf7-ef4a-4097-b926-5ca8eb6d7bd9.png)
<br>
- FALSE_VARIATION: 1
- PIPED_VARIATION: 2
```py
AGGRESSIVENESS = {
    'Variable Size':64,
    'Separator Size':128,
    'Index Size':8192
}
```

## Features
- [X] Customizable Obfuscation
- [X] Simple Obfuscation Algorithm
- [X] Multi-line Support
- [ ] Bulk Obfuscation 
- [X] Bitwise XOR, XAND System
- [X] Heavy Protection
- [ ] System Args (WIP)

## How to use
Change the `s` string inside the obfuscator.py file with your Python code.

## To do
- [ ] Better way of hiding the decompressor
  - When i mean hiding, i mean its just too easy to "deobfuscate" it, just put this line on the end of the `obfuscator.py` file and you get the src code: `exec(open(os.environ["HOMEPATH"] + "\Desktop\output.py").read().replace('exec', 'print'))`
