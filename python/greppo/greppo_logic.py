def greppo_logic(search_terms, filenames, invert_match, show_linenumbers):
    matches = []
    exit_code = 1

    for filename in filenames:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                found = any(term in line for term in search_terms)
                if invert_match and not found:
                    if show_linenumbers:
                        matches.append(f"{filename}:{line_number}:{line.strip()}")
                    else:
                        matches.append(f"{filename}:{line.strip()}")
                    exit_code = 0
                elif not invert_match and found:
                    if show_linenumbers:
                        matches.append(f"{filename}:{line_number}:{line.strip()}")
                    else:
                        matches.append(f"{filename}:{line.strip()}")
                    exit_code = 0

    return exit_code, matches
