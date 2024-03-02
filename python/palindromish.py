def palindromish(sekvens, grad=None):
    # kontrollera att sekvens är en sträng eller en lista
    if type(sekvens) not in [
        str,
        list,
    ]:
        return False, "sekvensen måste vara en sträng eller en lista"

    # kontrollera att grad är ett heltal eller inget alls
    if grad is not None and type(grad) is not int:
        return False, "grad måste vara ett heltal eller inget alls"

    # om grad saknas eller är större än halva längden av sekvensen, justera till halva längden av sekvensen
    n = len(sekvens)
    if grad is None or grad > n // 2:
        grad = n // 2

    # sekvens[:grad] tar de första tecknen definierat av grad
    # sekvens[-grad:][::-1] tar de sista tecknen definierat av grad och vänder på dem
    # om de två delarna är lika returneras True, om inte retuneras False

    # utför kontrollen
    return sekvens[:grad] == sekvens[-grad:][::-1]


if __name__ == "__main__":
    # Skriv exempel på körningar av funktionen här

    # Exempel:
    print(palindromish("radar", 2))
    print(palindromish([1, 2, 3, 2, 1], 3))
    print(palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4))
    print(palindromish("example", 3))
    print(palindromish("naturrutan"))
    print(palindromish(""))
    print(palindromish("kajak", 1000))
    print(palindromish("solros", 2))
    print(palindromish("solros", 3))
