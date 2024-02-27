"""
x = type(5)
print(x)

s = 'hejsan hoppsan'
l = [100,200,300,400,500,600]

s_tre = s[:3]
s_tre_sista = s[-3:]

l_tre = l[:3]
l_tre_sista = l[-3:]
"""

# refeerence by value
a = ["a", "b", "c"]
b = a[:]
e = a.copy()

spara = b.pop()

c = 1
d = c
d += 1
