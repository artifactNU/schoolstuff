import collections.abc


class InvalidSubstitutionCipher(Exception):
    pass


# definierar en klass som tar en lista av tupler som argument
class SubstitutionCipher:
    def __init__(self, map: [(str, str)]):  # type: ignore

        # validera att map är en sekvens
        if not isinstance(map, collections.abc.Sequence):
            # om map inte är en sekvens, kasta ett TypeError
            raise TypeError("map måste vara en sekvens")

        # skapa en dict som för varje tuple i map-listan kommer
        # lägga till ett key-value par där nyckeln är det första tecknet (tuple[0])
        # och värdet är det andra tecknet (tuple[1])
        # detta representerar krypteringsmappningen
        self.forward_map = {}

        # skapa ytterligare en dict som för varje tuple i map-listan kommer
        # lägga till ett key-value par där nyckeln är det andra tecknet (tuple[1])
        # och värdet är det första tecknet (tuple[0])
        # detta representerar dekrypteringsmappningen
        self.reverse_map = {}

        # loopa igenom varje tuple i map och validera att varje tuple innehåller två strängar av längd 1
        for item in map:
            # om något av villkoren nedan inte uppfylls, kasta ett undantag av typen InvalidSubstitutionCipher
            # validera att varje element i map är en tuple av längd 2
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("map måste innehålla tupler av längd 2")
            # validera att varje element i tuple är en sträng
            if not isinstance(item[0], str) or not isinstance(item[1], str):
                raise TypeError("båda elementen i tuple måste vara strängar")
            # validera att varje element i tuple är en sträng av längd 1
            if len(item[0]) != 1 or len(item[1]) != 1:
                raise ValueError(
                    "båda elementen i tuple måste vara strängar av längd 1"
                )
            # validera att inget tecken i map[0] eller map[1] förekommer mer än en gång
            if item[0] in self.forward_map or item[1] in self.reverse_map:
                raise InvalidSubstitutionCipher(
                    "en bokstav kan inte förekomma mer än en gång i map[0] eller map[1]"
                )

            # hantera stora och små bokstäver
            a, b = item
            self.forward_map[a.lower()] = b.lower()
            self.forward_map[a.upper()] = b.upper()
            self.reverse_map[b.lower()] = a.lower()
            self.reverse_map[b.upper()] = a.upper()

            # lägg till varje element i map[0] och map[1] i forward_map
            self.forward_map[item[0]] = item[1]
            # lägg till varje element i map[1] och map[0] i reverse_map
            self.reverse_map[item[1]] = item[0]

    # definiera en metod som tar en sträng som argument och returnerar en sträng
    def substitute(self, text: str) -> str:
        # validera att text är en sträng
        if not isinstance(text, str):
            raise TypeError("text måste vara en sträng")
        # byt ut varje tecken enligt forward_map och reverse_map
        return "".join(
            self.forward_map.get(c, self.reverse_map.get(c, c)) for c in text
        )


if __name__ == "__main__":

    cipher = SubstitutionCipher([("a", "m"), ("b", "n")])
    encrypted = cipher.substitute("Abba")
    print(encrypted)  # output: mnnm
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # output: abba

    cipher = SubstitutionCipher([])
    encrypted = cipher.substitute("hello")
    print(encrypted)  # output: hello
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # output: hello

    try:
        cipher = SubstitutionCipher([("a", "m"), ("b", "n"), ("a", "o")])
    except InvalidSubstitutionCipher as e:
        print(f"Invalid substitution detected: {e}")

    mapping = list(zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"))
    cipher = SubstitutionCipher(mapping)
    text = "JACK AND JILL WENT UP THE HILL"
    encrypted = cipher.substitute(text)
    print(encrypted)  # output: WNPX NAQ WVYY JRAG HC GUR UVYY
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # output: JACK AND JILL WENT UP THE HILL

    cipher = SubstitutionCipher([("s", "z"), ("i", "l"), ("m", "n"), ("o", "0")])
    encrypted = cipher.substitute("Simon")
    print(encrypted)  # output: zln0m
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # output: simon

    # Exempel på felmeddelanden:

    # ---------------------------------------------------------------------------

    # output: TypeError "map måste innehålla tupler av längd 2":

    # cipher = SubstitutionCipher([("a", "m", "n"), ("b", "n")])
    # encrypted = cipher.substitute("Abba")
    # print(encrypted)
    # decrypted = cipher.substitute(encrypted)
    # print(decrypted)

    # ---------------------------------------------------------------------------

    # output: TypeError "båda elementen i tuple måste vara strängar":

    # cipher = SubstitutionCipher([("a", 1), ("b", "n")])
    # encrypted = cipher.substitute("Abba")
    # print(encrypted)
    # decrypted = cipher.substitute(encrypted)
    # print(decrypted)

    # ---------------------------------------------------------------------------

    # output: ValueError "båda elementen i tuple måste vara strängar av längd 1":

    # cipher = SubstitutionCipher([("aa", "m"), ("b", "n")])
    # encrypted = cipher.substitute("Abba")
    # print(encrypted)
    # decrypted = cipher.substitute(encrypted)
    # print(decrypted)

    # ---------------------------------------------------------------------------

    # output: InvalidSubstitutionCipher "en bokstav kan inte förekomma mer än en gång i map[0] eller map[1]":

    # cipher = SubstitutionCipher([("a", "m"), ("b", "n"), ("a", "o")])
    # encrypted = cipher.substitute("Abba")
    # print(encrypted)
    # decrypted = cipher.substitute(encrypted)
    # print(decrypted)

    # ---------------------------------------------------------------------------

    # output: TypeError "text måste vara en sträng":

    # cipher = SubstitutionCipher([("1", "z"), ("2", "l"), ("3", "n"), ("4", "0")])
    # encrypted = cipher.substitute(1234)
    # print(encrypted)  # Expected output: zln0m
    # decrypted = cipher.substitute(encrypted)
    # print(decrypted)  # Expected output: simon

    # ---------------------------------------------------------------------------
