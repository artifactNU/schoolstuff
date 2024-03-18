import greppo_logic


def test_greppo_logic():
    test_cases = [
        (
            ["one", "two"],
            ["filnamn1"],
            False,
            False,
            (0, ["filnamn1:one", "filnamn1:two"]),
        ),
        (
            ["o"],
            ["filnamn1"],
            False,
            False,
            (0, ["filnamn1:one", "filnamn1:two", "filnamn1:four"]),
        ),
        (
            ["o"],
            ["filnamn2"],
            False,
            True,
            (0, ["filnamn2:1:boat", "filnamn2:4:helicopter", "filnamn2:5:rocket"]),
        ),
        (
            ["e"],
            ["filnamn1", "filnamn2"],
            True,
            True,
            (
                0,
                [
                    "filnamn1:2:two",
                    "filnamn1:4:four",
                    "filnamn2:1:boat",
                    "filnamn2:2:car",
                ],
            ),
        ),
        (["flower"], ["filnamn1", "filnamn2"], False, True, (1, [])),
    ]

    for search_terms, filenames, invert_match, show_linenumbers, expected in test_cases:
        print(
            f"Running test: {search_terms}, {filenames}, {invert_match}, {show_linenumbers}, expected {expected}"
        )
        try:
            result = greppo_logic.greppo_logic(
                search_terms, filenames, invert_match, show_linenumbers
            )
            assert (
                result == expected
            ), f"For {search_terms}, {filenames}, {invert_match}, {show_linenumbers}, expected {expected} but got {result}"
        except Exception as e:
            print(f"An error occurred: {e}")
    print("All tests passed!")


if __name__ == "__main__":
    test_greppo_logic()
