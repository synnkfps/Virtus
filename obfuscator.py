import sys
sys.getdefaultencoding()

transformer = {
    '1': '\'1\'',
    '2': '\'2\'',
    '3': '\'3\'',
    '4': '\'4\'',
    '5': '\'5\'',
    '6': '\'6\'',
    '7': '\'7\'',
    '8': '\'8\'',
    '9': '\'9\'',
    '0': '\'0\'',

    'a': 'str(hash)[-2**2**1**69420]',
    'b': 'str(hash)[True**True+False+False**1**(True**69*69**420)]',
    'c': 'str(hash)[-int(eval("12-eval(\'True**1**129391231239129391231923912939129312.31297361278361287361728367811\')"))]',
    'd': 'str(id)[-True-True+True-True]',
    'e': "str(str(str(BufferError)*len(str(MemoryError)))[75-int(eval('True+True+True+True+True+True'))+int(eval('True+True+True+True+True+True-False+True+True+True'))+69-420+6+9-True]).lower()",
    'f': rf"'0x256f勒屁艾娜伊杰艾 开儿 迪艾西艾迪艾伊 艾 吉诶哦伊 屁 弗勒 艾屁西艾 儿勒屁艾娜伊杰艾 开儿 迪艾西艾 勒艾 儿勒屁艾 开勒屁哦吉 儿勒屁 艾屁西艾艾艾弗 弗勒迪 诶娜娜 开勒哦吉伊艾艾屁西艾伊艾'[{'abcdefghijklmnopqrstuvwxyz'.index(str(str(str(BufferError)*len(str(MemoryError)))[75-int(eval('True+True+True+True+True+True'))+int(eval('True+True+True+True+True+True-False+True+True+True'))+69-420+6+9-True]).lower())}+1]",
    'g': f"'0x2567gew78qeh8qwh78ehq789w§§§§§§§§ªºªef'[{'abcdefghijklmnopqrstuvwxyz'.index(str(str(str(BufferError)*len(str(MemoryError)))[75-int(eval('True+True+True+True+True+True'))+int(eval('True+True+True+True+True+True-False+True+True+True'))+69-420+6+9-True]).lower())}+1+1]",
    'h': "'§0x1123abc⎲h.256㊈'[(True**1)+len('⒣⒠⒧⒧⒪!⎲⎲⎲⎲')]",
    'i': "str(BrokenPipeError)[15+(True**5)-1]",
    'j': '"0x256 0x512hj0a"[-3]',
    'k': "'≧⏝≦伊Gk107事㌹f勒屁艾娜伊杰艾 开儿 迪艾西艾迪艾ｼｲｩ ｲｮｱｪ 伊杰艾㊆g㊆㊋ｱｮ㊘'[True*5]",
    'l':'str(lambda x:x)[11]',
    'm': 'str(ModuleNotFoundError).lower()[(True+True+True+True)*(True+True)]',
    'n': "'abcdefghijklmnopqrstuvwxyz'[len('abcdefghijklmnopqrstuvwxyz')-len('abcdefghijklmnopqrstuvwxyz')+len('abcdefghijklmnopqrstuvwxyz')-13]",
    'o': 'str(ModuleNotFoundError).lower()[(True+True+True+True)*(True+True)+True]',
    'p': "'abcdefghijklmnopqrstuvwxyz'[BrokenPipeError.__basicsize__-100+3]", # 100+11 for python 3.7.8+
    'q': 'str(quit)[(True+True)**2]',
    'r': "'abcdefghijklmnopqrstuvwxyz'[hasattr.__sizeof__()-40+9]", # 40+1 for python 3.7.8+
    's': '\'s\'',
    't': 'str(TimeoutError)[14]'.strip(),
    'u': '\'u\'',
    'v': '\'v\'',
    'w':'\'w\'',
    'x':'\'x\'',
    'y':'\'y\'',
    'z':'\'z\'',
    '\\n': '\n',
    '\\t': '\t',
    ':': '\':\'',
    ',': '\',\'',
    ';':'\';\'',
    '+': '\'+\'',
    '.': '\'.\'',
    '*': '\'*\'',
    '=': '\'=\'',
    '\\': r'\\',
    '>': 'str(MemoryError)[-True]',
    '<': 'str(BrokenPipeError)[False]',
    ' ': 'str(MemoryError)[6]',
    '\'': r'str(object)[6-3-False-3+6+6-6+6-6-6+6-3-3-False+6+6-6+6-6-6+6-3-3+6-False+6-6+6-6-6+6-3-False-3+6+6-6+6-6-6+6-3-3+6+6-6-False+6-6-6+6-3-3+6+6-6+6-6-6+6+True]',
    '"': r'str(object)[6-3-False-3+6+6-6+6-6-6+6-3-3-False+6+6-6+6-6-6+6-3-3+6-False+6-6+6-6-6+6-3-False-3+6+6-6+6-6-6+6-3-3+6+6-6-False+6-6-6+6-3-3+6+6-6+6-6-6+6+True]',
    '[': "str(list(tuple(list(tuple([0x128, False]+[0x256, True]+[bytes('ordinalCoordinate', 'utf-16')])))))[False]",
    ']': "str(str(BlockingIOError)+str([]) + str(list(tuple(list(tuple([0x128, False]+[0x256, True]+[bytes('ordinalCoordinate', 'utf-16'), ])))))[False])[-2]",
    '(': 'str(tuple(list(([0o256, 0x123, 0x128, 0x512, 0x1024, 0x2048, 0x4096, 0x8192, 0x1691823, 0x32767febcdefaeaeaeae0f0f0f0f0fababe]))))[False]',
    ')': 'str(tuple(list(([0o256, 0x123, 0x128, 0x512, 0x1024, 0x2048, 0x4096, 0x8192, 0x1691823, 0x32767febcdefaeaeaeae0f0f0f0f0fababe]))))[-True]'
}

code = """
for i in range(10):
    for j in range(5):
        print(i*j, end=' ', sep=' ')
"""

stuff=[]
raw = ''''''

def obfuscate(str):
    tmp = []
    for i in str: tmp.append(transformer[i])
    return f'exec({"+".join(tmp)})'

s = ''

for i in code.splitlines():
    print(rf'{i}')
    raw += i + '\n'
    stuff.append(obfuscate(i)+'\n')

for i in stuff:
    if i!='exec()':
        #print('\n' in i)
        s+=i 

print(s)
print(raw)
exec(raw)
