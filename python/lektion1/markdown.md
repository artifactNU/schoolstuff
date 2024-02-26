# 1. Detta är min huvudrubrik
    Här är lite text som följer efter huvudrubriken.
## 2. Detta är en underrubrik
    Här är lite text som följer efter underrubriken.
3. En lista med några punkter
- punkt 1
- punkt 2
- punkt 3
4. En liten tabell med tre kolumner och fem rader
| Kolumn 1 | Kolumn 2 | Kolumn 3 |
|----------|----------|----------|
| Rad 1    | Rad 1    | Rad 1    |
| Rad 2    | Rad 2    | Rad 2    |
| Rad 3    | Rad 3    | Rad 3    |
| Rad 4    | Rad 4    | Rad 4    |
| Rad 5    | Rad 5    | Rad 5    |
5. Texten Zenuml-diagram
    title Secret
    Alice->Bob: Hello Bob, want to know a secret?
    Bob->Alice: Yes!
    Alice->Bob: Then share your public key!
6. Ett Mermaid-diagram av typen [Zenuml](https://mermaid.js.org/syntax/zenuml.html)
zenuml
    title Secret
    Alice->Bob: Hello Bob, want to know a secret?
    Bob->Alice: Yes!
    Alice->Bob: Then share your public key!
7. Texten Flowchart-diagram
    A[Message] --> B{Is it encrypted?}
    B -- Yes --> C[Decrypt]
    C --> D[Awnser]
    D --> B
    B -- No ----> E[End]
8. Ett Mermaid-diagram av typen [Flowchart](https://mermaid.js.org/syntax/flowchart.html)
flowchart TD
    A[Message] --> B{Is it encrypted?}
    B -- Yes --> C[Decrypt]
    C --> D[Awnser]
    D --> B
    B -- No ----> E[End]