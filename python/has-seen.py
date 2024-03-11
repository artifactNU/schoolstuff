observed = set()


def has_seen(obj: int | str) -> bool:
    if obj in observed:
        return True
    else:
        observed.add(obj)
        return False


if __name__ == "__main__":
    # Exempel:
    print(has_seen(1))
    print(has_seen("a"))
    print(has_seen(1))
    print(has_seen("a"))
