def wordfreq(text: str) -> dict:

    # splitta texten till en lista av ord
    words = text.split()
    # skapa en tom dictionary
    freq = {}
    # loopa igenom varje ord i listan
    for word in words:
        # om ordet redan finns i dict öka frekvensen med 1
        if word in freq:
            freq[word] += 1
        # annars lägg till ordet i dict med frekvensen 1
        else:
            freq[word] = 1
    # returnera dict
    return freq


if __name__ == "__main__":
    # Exempel:
    print(wordfreq("hej hej på dig"))
    print(wordfreq("ett två tre två"))
    print(wordfreq(""))
    print(wordfreq("python programmering python"))
    print(wordfreq("test test test"))
