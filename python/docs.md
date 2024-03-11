# Grundläggande förståelse för dokumentationen

## Language Reference

1. **If-satser:**

   If-satser i Python möjliggör villkorsstyrd exekvering av kod. Genom att använda if följt av ett villkor, kan man dirigera programflödet baserat på om villkoret utvärderas till True eller False. En if-sats kan utökas med elif och else för att hantera flera olika villkor.

#### BNF-notationen för if-satser är följande:

```
if_stmt ::=  "if" assignment_expression ":" suite
            ("elif" assignment_expression ":" suite)*
            ["else" ":" suite]
```

Här är `assignment_expression` en variabel som jämförs med ett annat värde, och `suite` är en sekvens av satser som exekveras om villkoret är sant.

#### Exempel på en if-sats som kollar om x är positivt, negativt eller noll:

```python
if x > 0:
     print("x är positivt")
 elif x < 0:
     print("x är negativt")
 else:
     print("x är noll")
```

2. **While-loopar:**

   While-loopar i Python används för att upprepa kod baserat på ett specifikt villkor. Så länge villkoret är sant, kommer koden inuti while-loopen att exekveras.

#### BNF-notationen för while-loopar är följande:

```
while_stmt ::=  "while" assignment_expression ":" suite
               ["else" ":" suite]
```

Här är `assignment_expression` ett villkor som utvärderas till True eller False, och `suite` är en sekvens av satser som exekveras så länge villkoret är sant.

#### Exempel på en while-loop som räknar upp till 5:

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

3. **For-loopar:**

   For-loopar i Python används för att iterera över sekvenser, såsom listor, strängar eller andra objekt.

#### BNF-notationen för for-loopar är följande:

```
for_stmt ::=  "for" target_list "in" starred_list ":" suite
               ["else" ":" suite]
```

Här är `target_list` en variabel som används för att lagra varje element i sekvensen och `starred_list` är själva sekvensen som ska itereras över.

#### Exempel på en for-loop som skriver ut namnen i en lista:

```python
names = ["Alice", "Bob", "Eve"]
for name in names:
    print(name)
```

## Standard Library

4. **Strängmetoder:**

   - `.capitalize()`: Används för att göra den första bokstaven i en sträng till stor bokstav och resten av strängen till små bokstäver.
   - `.upper()`: Används för att konvertera hela strängen till stora bokstäver.
   - `.split()`: Används för att dela upp en sträng i en lista av delsträngar baserat på ett visst separator-tecken.
   - `.join()`: Används för att sammanfoga en lista av strängar till en enda sträng, med ett visst separator-tecken mellan varje element.

#### Exempel på användning av strängmetoder:

```python
s = "hello, world"
   print(s.capitalize())  # Output: "Hello, world"
   print(s.upper())       # Output: "HELLO, WORLD"
   print(s.split(","))    # Output: ["hello", " world"]
words = ["hello", "world"]
   print(" ".join(words)) # Output: "hello world"
```

5. **Sekvenstyper och deras operationer:**

   - `list`: En lista är en ordnad samling av element som kan ändras
   - `tuple`: En tuple är en ordnad samling av element som inte kan ändras
   - `range`: En range är en sekvens av nummer som genereras

#### Exempel på användning av listor:

```python
# Skapa en lista
numbers = [1, 2, 3, 4, 5]
# Lägg till ett element
numbers.append(6)
# Ändra ett element
numbers[0] = 0
# Ta bort ett element
numbers.remove(3)
```

#### Exempel på tuple:

```python
# Skapa en tuple
coordinates = (3, 4)
# Försök ändra ett element (ger felmeddelande)
coordinates[0] = 5
```

#### Exempel på användning av range:

```python
# Skapa en range
numbers = range(5)
# Skriv ut varje nummer i rangen (0, 1, 2, 3, 4)
for number in numbers:
   print(number)
```

6. **Ordböcker:**

   En ordbok i Python är en samling av key-value par där varje nyckel är unik. För att skapa en ordbok används måsvingar `{}` och key-value par separeras med kolon `:`. Nyckeln används för att hämta värdet från ordboken. För att lägga till ett nytt key-value par eller ändra ett värde, används indexering med nyckeln.

#### Exempel på användning av ordböcker:

```python
person = {"name": "Alice", "age": 25, "city": "Stockholm"}
# Lägg till ett nytt key-value par
person["email"] = "alice@email.com"
# Ändra ett värde
person["age"] = 26
# Iterera över nycklar och värden
for key, value in person.items():
    print(key, value)
```

7. **Inbyggda funktioner:**

   - `input()`: Används för att ta in användarinput från terminalen.
   - `max()`: Används för att hitta det största värdet i en sekvens av nummer.
   - `min()`: Används för att hitta det minsta värdet i en sekvens av nummer.
   - `len()`: Används för att hitta längden på en sekvens, såsom en sträng, lista eller tuple.

#### Exempel på ovansående funktioner:

```python
name = input("Vad är ditt namn? ")
print("Hej,", name)
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1
print(len(numbers))  # Output: 11
```
