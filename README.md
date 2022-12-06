# Virtus
Powerful Python Obfuscator, capable of obfuscate (only) single Python files, using a new obfuscation algorithm.

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
