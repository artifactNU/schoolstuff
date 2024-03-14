# skapa ett set som sparar objekt som passerar funktionen
observed = set()


# definiera en funktion som tar ett objekt som argument
def has_seen(obj: int | str) -> bool:
    # om objektet redan finns i observed, returnera True
    if obj in observed:
        return True
    # om objektet inte finns i observed, lägg till objektet och returnera False
    else:
        observed.add(obj)
        return False


if __name__ == "__main__":
    # Exempel:
    print(has_seen(1))
    print(has_seen("a"))
    print(has_seen(0))
    print(has_seen("abra kadabra"))
    print(has_seen(1))
    print(has_seen("a"))
    print(has_seen(0))
    print(has_seen("abra kadabra"))
