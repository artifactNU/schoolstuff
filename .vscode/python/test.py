# Variabler
name = "John"
age = 25
height = 175.5

# Array
numbers = [1, 2, 3, 4, 5]

# Loopar
print("Utskrift med for-loop:")
for num in numbers:
    print(num)

print("Utskrift med while-loop:")
# En while-loop som skriver ut siffrorna 1 till 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Villkorskonstruktioner
if age >= 18:
    print(f"{name} är myndig.")
else:
    print(f"{name} är inte myndig.")

# Klasser och objekt
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display_info(self):
        print(f"Namn: {self.name}, Ålder: {self.age}, Längd: {self.height} cm")

# Skapa ett objekt av Person-klassen
person1 = Person(name, age, height)

# Anropa en metod på objektet
person1.display_info()

# En annan metod för att ändra ålder med ett extra argument
def increase_age(person, years):
    person.age += years

# Anropa metoden för att öka åldern med ett extra argument
increase_age(person1, 5)

# Visa uppdaterad information
person1.display_info()
