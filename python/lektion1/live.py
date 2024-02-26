s = 'First line.\nSecond line.'  # \n means newline

print (s)

print(r'C:\some\name')  # here \n means newline! use r before the quote to avoid this

lista = """\
Alpha
Beta
Gamma
"""

print(lista)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

res = 3 * 'un' + 'ium'
print(res)

text = ('Put several strings within parentheses '

        'to have them joined together.')
print(text)

word = 'Python'
r = word[2]
r2 = word[-6]
r3 = word[0]
r4 = word[-1]  # last character

# slicing

start_pos = 1
slut_pos = 3
slicad = word[start_pos:slut_pos]
slicad2 = word[:slut_pos]
slicad3 = word[start_pos:]
slicad4 = word[:]

# slicing kombinerat med sammanslagning
slicad5 = word[:2] + word[2:]

# längd av en sträng
sa = 'supercalifragilisticexpialidocious'
slenght = len(sa)