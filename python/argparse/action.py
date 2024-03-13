import argparse

parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument("--version", action="version", version="%(prog)s 2.0")
parser.add_argument("--fisk", action="store_const", const=42)
r = parser.parse_args()
print(r)
