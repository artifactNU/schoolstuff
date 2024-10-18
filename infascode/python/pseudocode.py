# Mål: byt ut repeterande specialtecken som :,.; och blanksteg mot endast ett tecken
# i en fil och skriv ut det till stdout.


# Filen körbar med: chmod +x non_repeating_chars.py

# om användaren inte har angett något argument eller fler än ett argument
#       skriv ett felmeddelande till stderr
#       avsluta med statuskod

# input = argument från användaren

# om input inte är en fil eller inte kan läsas
#       skriv ett felmeddelande till stderr
#       avsluta med statuskod

# file_lines = läs in alla rader i input till en lista med strängar

# non_repeting_chars = ":.; "

# för varje rad i file_lines hitta repeterande non_repeting_chars och byt ut dem mot endast ett sådant tecken
#       för varje part av line där non_repeting_chars repeteras
#         för varje part i parts
#           line =
#             - Den nuvarande line, med delen part utbytt mot endast ett tecken
#             - Det tecken tas från första positionen i part
#
# skriv ut den nya raden till stdout
# avsluta med statuskod
