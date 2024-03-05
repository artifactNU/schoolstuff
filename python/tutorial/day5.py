# # globala variablar

# x = 10
# y = 1337


# def minfunction():
#     x = 99
# #    global y
#     y = 420

#     print(f"Hej, från min funktion är x = {x} och y = {y}")


# minfunction()
# print(f"Utanför funktionen är x = {x} och y = {y}")
# ----------------------------

# Nonlocal

# def yttre(x):
#     def inre():
#         nonlocal x
#         x = 69
#         print(f"inre {x}")

#     inre()
#     print(f"yttre {x}")


# yttre(10)
# -----------------------------

##OBS

# def plus(x, y=0, z):
#     return x + y + z

# # Positionella argument
# print(plus(10, 20 ,30))

# # Keyword argument
# print(plus(10, z=69))

# ----------------------------

# def function(a):
#     print(a)

# function(10)
# function(a=10)

# ----------------------------

# def multi_greet(*alla_namn, greeting="Hej"):
#     for namn in alla_namn:
#         print(f"{greeting} {namn}!")
#     pass

# multi_greet("Kent", "Ulla")
# # Hej Kent!
# # Hej Ulla!

# -----------------------------

# valfritt antal argument


# def calculate(*args, operator="+"):
#     if operator == "+":
#         return sum(args)
#     else:
#         operator == "-"
#         return args[0] - sum(args[1:])


# print(calculate(1, 2, 3, 4))  # Förväntat returvärde: 10
# print(calculate(1, 2, 3, 4, operator="+"))  # Förväntat returvärde: 10
# print(calculate(10, 1, 2, operator="-"))  # Förväntat returvärde: 7
# print(calculate(5, 5, operator="-"))  # Förväntat returvärde: 0
# print(calculate())  # Förväntat returvärde: 0 (inga argument)

# ------------------------------

# Data structure

# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# #fruits.reverse()
# #fruits.sort()
# #fruits.pop()
# kiwi_index = fruits.index("kiwi")

# #"Alfabetisk" ordning
# mi = min(fruits)
# ma = max(fruits)


# if "apelsin" in fruits:
#     print("Det finns orange")
# else:
#     print("Det finns inte")

# -------------------------------

# Stacks
