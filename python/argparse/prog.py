import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument(
#     "-v", "--verbose", help="increase output verbosity", action="store_true"
# )
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbose", action="store_true", help="increase output verbosity"
# )
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity"
# )
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display the square of a given number")
# parser.add_argument(
#     "-v", "--verbosity", action="count", help="increase output verbosity"
# )
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbosity", action="count", help="increase output verbosity"
# )
# args = parser.parse_args()
# answer = args.square**2

# # bugfix: replace == with >=
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int, help="display a square of a given number")
# parser.add_argument(
#     "-v", "--verbosity", action="count", default=0, help="increase output verbosity"
# )
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)

# -----------

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y

# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print(f"{args.x} to the power {args.y} equals {answer}")
# else:
#     print(f"{args.x}^{args.y} == {answer}")

# -----------

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "-v", "--verbose", action="store_true", help="increase output verbosity"
)
group.add_argument("-q", "--quiet", action="store_true", help="only output result")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
