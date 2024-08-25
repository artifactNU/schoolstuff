# definiera en funktion som tar ett träd som input och returnerar en tuple med koordinater och värden för varje lövnod i trädet.
def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # skapa en tom lista för resultaten
    result = []

    # iterera över varje key-value par i trädet
    for key, value in tree.items():

        # lägg till den aktuella nyckeln till de aktuella koordinaterna
        new_coord = current_coord + (key,)

        # om värdet är en dict indikerar det ett underträd
        # anropa funktionen rekursivt på underträdet och utöka resultatslistan
        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))

        # om värdet inte är en dict indikerar det en lövnod
        # lägg till koordinaterna och värdet till resultatslistan
        else:
            result.append((new_coord, value))

    # konvertera resultatslistan till en tuple och returnera den
    return tuple(result)


if __name__ == "__main__":
    # Exempel:
    print(treecoords({"a": 1, "b": 2}))
    print(treecoords({"x": {"y": 3}, "z": 4}))
    print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
    print(treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}))
    print(treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}))
