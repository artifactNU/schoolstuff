def greppo_logic(search_terms, filenames, invert_match, show_linenumbers):
    matches = []  # lagra matchningar
    exit_code = 1  # initialisera exit_code till 1

    for filename in filenames:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                # kontrollera om någon av söktermerna finns i den aktuella raden
                found = any(search_term in line for search_term in search_terms)

                # om invert_match är True och termen inte hittades, eller om invert_match är False och termen hittades
                if (invert_match and not found) or (not invert_match and found):
                    # om show_linenumbers är True:
                    # lägg till filnamnet, radnumret och raden till matchningar
                    if show_linenumbers:
                        matches.append(f"{filename}:{line_number}:{line.strip()}")
                    # om show_linenumbers är False:
                    # lägg endast till filnamnet och raden till matchningar
                    else:
                        matches.append(f"{filename}:{line.strip()}")
                    # ändra exit_code till 0 eftersom en matchning hittades
                    exit_code = 0

    return exit_code, matches


if __name__ == "__main__":
    pass
