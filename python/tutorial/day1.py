# new line
s = 'First line.\nSecond line.'  # \n means newline

print (s)

print(r'C:\some\name')  # here \n means newline! use r before the quote to avoid this

# multiline
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

# indexering
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

# listor
squares = [1, 4, 9, 16, 25]
squaresid = squares
squares2 = squares[:]

squares2.append(36)

del squares2[3]

#sista = squares[-1]
#nylista = squares[1:4]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(type(letters))
letters[2:5] = ['C', 'D', 'E']