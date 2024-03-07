# öppna filen
handtag = open("fil.txt", "r", encoding="utf-8")

# läser in filen i en lista
innehall = handtag.readlines()

print(innehall)
print(type(innehall))

# stäng filen
handtag.close()
