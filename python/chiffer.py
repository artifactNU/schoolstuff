import collections.abc


class InvalidSubstitutionCipher(Exception):
    pass


# definiera en klass SubstitutionCipher som tar en lista av tupler som argument i konstruktorn
class SubstitutionCipher:
    def __init__(self, map: [(str, str)]):  # type: ignore

        # validera att map är en sekvens
        if not isinstance(map, collections.abc.Sequence):
            # om map inte är en sekvens, kasta ett TypeError
            raise TypeError("map must be a sequence")

        # skapa en dictionary som mappar varje tecken i map[0] till map[1] och vice versa
        self.forward_map = {}
        # skapa en dictionary som mappar varje tecken i map[1] till map[0] och vice versa
        self.reverse_map = {}
        # loopa igenom varje tuple i map och validera att varje tuple innehåller två strängar av längd 1

        for item in map:
            # om något av villkoren nedan inte uppfylls, kasta ett undantag av typen InvalidSubstitutionCipher
            # validera att varje element i map är en tuple av längd 2
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("map must contain tuples of length 2")
            # validera att varje element i tuple är en sträng
            if not isinstance(item[0], str) or not isinstance(item[1], str):
                raise TypeError("both elements of tuple must be strings")
            # validera att varje element i tuple är en sträng av längd 1
            if len(item[0]) != 1 or len(item[1]) != 1:
                raise ValueError("both elements of tuple must be single characters")
            # validera att inget tecken i map[0] eller map[1] förekommer mer än en gång
            if item[0] in self.forward_map or item[1] in self.reverse_map:
                raise InvalidSubstitutionCipher(
                    "a character appears more than once in the map"
                )

            # lägg till varje element i map[0] och map[1] i forward_map
            self.forward_map[item[0]] = item[1]
            # lägg till varje element i map[1] och map[0] i reverse_map
            self.reverse_map[item[1]] = item[0]

    # definiera en metod substitute som tar en sträng som argument och returnerar en sträng
    def substitute(self, text: str) -> str:
        # validera att text är en sträng
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        # byt ut varje tecken enligt forward_map och reverse_map
        return "".join(
            self.forward_map.get(c, self.reverse_map.get(c, c)) for c in text
        )


if __name__ == "__main__":
    cipher = SubstitutionCipher([("a", "m"), ("b", "n")])
    encrypted = cipher.substitute("abba")
    print(encrypted)  # Expected output: mnnm
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # Expected output: abba

    cipher = SubstitutionCipher([])
    encrypted = cipher.substitute("hello")
    print(encrypted)  # Expected output: hello
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # Expected output: hello

    try:
        cipher = SubstitutionCipher([("a", "m"), ("b", "n"), ("a", "o")])
    except InvalidSubstitutionCipher as e:
        print(f"Invalid substitution detected: {e}")

    mapping = list(zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"))
    cipher = SubstitutionCipher(mapping)
    text = "JACK AND JILL WENT UP THE HILL"
    encrypted = cipher.substitute(text)
    print(encrypted)  # Expected output: WNPX NAQ WVYY JRAG HC GUR UVYY
    decrypted = cipher.substitute(encrypted)
    print(decrypted)  # Expected output: JACK AND JILL WENT UP THE HILL
