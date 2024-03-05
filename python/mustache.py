def mustache(string: str, **vars: str):
    for key, value in vars.items():
        string = string.replace("{{" + key + "}}", value)
    return string


print("-------------")

print(
    mustache(
        "Hej {{name}}! Välkommen till {{place}}.", name="Alice", place="Wonderland"
    )
)

print()

print(
    mustache(
        """Kära {{name}},
Vi vill påminna {{name}} om mötet imorgon.""",
        name="Bob",
    )
)

print()

print(mustache("Detta är en text utan nyckelord att ersätta."))

print()

print(
    mustache(
        "Hej {{namn}}! Vi tror att {{name}} {{produkt}} skulle passa dig!",
        namn="Bo",
        produkt="hasch",
        name="Trottes",
    )
)

print("-------------")
