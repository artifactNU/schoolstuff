# Detta är min huvudrubrik

    Här är lite text som följer efter huvudrubriken.

## Detta är en underrubrik

    Här är lite text som följer efter underrubriken.

## En lista med några punkter

- punkt 1
- punkt 2
- punkt 3

## En tabell med tre kolumner och fem rader

| Kolumn 1 | Kolumn 2 | Kolumn 3 |
| -------- | -------- | -------- |
| Rad 1    | Rad 1    | Rad 1    |
| Rad 2    | Rad 2    | Rad 2    |
| Rad 3    | Rad 3    | Rad 3    |
| Rad 4    | Rad 4    | Rad 4    |
| Rad 5    | Rad 5    | Rad 5    |

## Texten för sequence-diagram

    title Secret Message
    Alice->>Bob: Hello Bob, want to know a secret?
    Bob->>Alice: Yes!
    Alice->>Bob: Then share your public key!

## Sequence-diagram

```mermaid
sequenceDiagram
title Secret Message
Alice->>Bob: Hello Bob, want to know a secret?
Bob->>Alice: Yes!
Alice->>Bob: Then share your public key!
```

## Texten för Flowchart-diagram

    A[Message] --> B{Is it encrypted?}
    B -- Yes --> C[Decrypt]
    C --> D[Anwser]
    D --> B
    B -- No ----> E[End]

## Flowchart-diagram

```mermaid
flowchart TD
    A[Message] --> B{Is it encrypted?}
    B -- Yes --> C[Decrypt]
    C --> D[Anwser]
    D --> B
    B -- No ----> E[End]
```
