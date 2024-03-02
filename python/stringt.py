def stringt(*args, sep=" ", end="\n"):
    string = ""
    for argument in args:
        # konvertera argument till str och lägg till separatorn
        string += str(argument) + sep
    # ta bort den sista separatorn och hantera sep=""
    if sep != "":
        string = string[: -len(sep)]
    # returnera med end
    return string + end


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    #
    # Exempel:
    print(stringt("a", "b", "c", [1, 2, 3]))
    print(stringt("a", "b", "c", [1, 2, 3], sep=";"))
    print(stringt("a", "b", "c", [1, 2, 3], sep="?", end="!"))
    print(stringt(1, 2, 3, ["hej", "på", "dig"]))
    print(stringt(1.4, 2.5, 3.6, ["1", "på", "6.9"]))
    print(stringt("Hej", "världen", sep=", ", end="!"))
    print(stringt("Python", "är", "kul"))
    print(stringt("En", "två", "tre", sep=" - "))
    print(stringt("Slut", end="."))
    print(stringt("Ett", "argument", sep=""))
    print(stringt("Ensam"))
