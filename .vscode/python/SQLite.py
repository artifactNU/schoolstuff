import sqlite3

'''
1. Skapa en databas och en tabell:

    En SQLite-databasfil med namnet "exempel.db" kommer att skapas om den inte redan finns.
    En tabell med namnet "users" kommer att skapas om den inte redan finns. Den kommer att ha kolumner för id, namn och ålder.

2. Lägga till en användare (Create):

    En ny rad kommer att läggas till i "users"-tabellen med informationen om användaren "John Doe" och ålder 30.

3. Hämta och skriva ut alla användare (Read):

    En SELECT-fråga kommer att köras för att hämta alla användare från "users"-tabellen.
    Information om användarna kommer att skrivas ut till terminalen.

4. Uppdatera åldern för användaren med id 1 (Update):

    En UPDATE-fråga kommer att köras för att ändra åldern för användaren med id 1 till 35.

5. Radera användaren med id 1 (Delete):

    En DELETE-fråga kommer att köras för att radera användaren med id 1 från "users"-tabellen.

6. Hämta och skriva ut användare igen (Read):

    En SELECT-fråga kommer att köras för att hämta alla användare från "users"-tabellen igen.
    Uppdaterad information om användarna kommer att skrivas ut till terminalen.

7. Importera data från en SQL-fil (Import):

    Innehållet i filen "import_file.sql" kommer att köras som en SQL-skript för att importera data till databasen.

8. Exportera data till en SQL-fil (Export):

    En SQL-skript som representerar databasens innehåll kommer att skrivas till filen "export_file.sql"
'''


# 1. Skapa en databas och en tabell
def create_database():
    conn = sqlite3.connect('exempel.db')    # Steg 1
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# 2. Lägg till en användare (Create)
def insert_user(name, age):
    conn = sqlite3.connect('exempel.db')    # Steg 2
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

# 3. Hämta och skriv ut alla användare (Read)
def get_users():
    conn = sqlite3.connect('exempel.db')    # Steg 3
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# 4. Uppdatera åldern för användaren med id 1 (Update)
def update_user_age(user_id, new_age):
    conn = sqlite3.connect('exempel.db')    # Steg 4
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
    conn.commit()
    conn.close()

# 5. Radera användaren med id 1 (Delete)
def delete_user(user_id):
    conn = sqlite3.connect('exempel.db')    # Steg 5
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

# 6. Importera data från en SQL-fil (Import)
def import_data_from_file(filename):
    conn = sqlite3.connect('exempel.db')  # Steg 7
    cursor = conn.cursor()
    with open(filename, 'r') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)
    conn.commit()
    conn.close()

# 7. Exportera data till en SQL-fil (Export)
def export_data_to_file(filename):
    conn = sqlite3.connect('exempel.db')  # Steg 8
    with open(filename, 'w') as file:
        for line in conn.iterdump():
            file.write('%s\n' % line)
    conn.close()

# Skapa databasen och tabellen
create_database()

# Lägg till en användare
insert_user("John Doe", 30)

# Hämta och skriv ut alla användare
users = get_users()
print("Alla användare:")
for user in users:
    print(user)

# Uppdatera åldern för användaren med id 1
update_user_age(1, 35)

# Hämta och skriv ut användare igen
users = get_users()
print("\nUppdaterade användare:")
for user in users:
    print(user)

# Radera användaren med id 1
delete_user(1)

# Hämta och skriv ut användare efter radering
users = get_users()
print("\nÅterstående användare:")
for user in users:
    print(user)

# Importera data från en SQL-fil
import_data_from_file('import_file.sql')

# Exportera data till en SQL-fil
export_data_to_file('export_file.sql')
