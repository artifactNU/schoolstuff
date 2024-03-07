# Definiera en funktion som tar ett träd och en tuple av koordinater
def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # Initiera en tom lista för att lagra resultaten
    result = []

    # iterera över varje key-value par i trädet
    for key, value in tree.items():

        # lägg till den aktuella nyckeln till de aktuella koordinaterna
        new_coord = current_coord + (key,)

        # Om värdet är en ordbok (indikerar ett underträd)
        # Anropa funktionen rekursivt på underträdet och utöka resultatslistan
        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))

        # Om värdet inte är en ordbok (indikerar en lövnod)
        # Lägg till koordinaterna och värdet till resultatslistan
        else:
            result.append((new_coord, value))

    # Konvertera resultatslistan till en tuple och returnera den
    return tuple(result)


print(treecoords({"a": 1, "b": 2}))
