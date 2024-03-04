# listhanterare

movies = ("Filmer", ["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"])
todo = ("Att göra", ["Städa", "Handla", "Träna"])
bread = ("Bröd", ["Rågbröd", "Kavring", "Limpa"])

lists = [movies, todo, bread]

list_index = 0

while True:
    titel, lista = lists[list_index]
    print("----------------")
    print(f"Lista: {titel}")
    print("Val: ")
    print("1 - Lägg till rad i listan")
    print("2 - Skriv ut alla rader i listan")
    print("3 - Gå till nästa lista")
    print("a - Avsluta")

    choice = input("Ange Val: ")

    if choice == "1":
        rad = input("Skriv det du vill lägga till i listan: ")
        lista.append(rad)
    elif choice == "2":
        print(f"Lista: {titel}")
        print("----------------")
        for rad in lista:
            print(rad)
    elif choice == "3":
        list_index = (list_index + 1) % len(lists)
    elif choice == "a":
        break
    else:
        print("Ogiltigt val")
print()
