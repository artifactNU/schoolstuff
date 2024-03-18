import argparse
from greppo_logic import greppo_logic


def main():
    parser = argparse.ArgumentParser(description="Search for text strings in files.")
    parser.add_argument(
        "filenames", metavar="F", type=str, nargs="+", help="one or more filenames"
    )
    parser.add_argument(
        "--search",
        metavar="S",
        type=str,
        nargs="+",
        help="string to search for in the files",
    )
    parser.add_argument(
        "-n",
        "--line-number",
        action="store_true",
        help="show line number for each match",
    )
    parser.add_argument(
        "-v", "--invert-match", action="store_true", help="invert the search"
    )
    parser.add_argument(
        "-q", "--quiet", "--silent", action="store_true", help="turn off prints"
    )

    args = parser.parse_args()

    exit_code, matches = greppo_logic(
        args.search, args.filenames, args.invert_match, args.line_number
    )

    if not args.quiet:
        for match in matches:
            print(match)

    return exit_code


if __name__ == "__main__":
    main()
