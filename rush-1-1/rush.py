import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    top_bottom = "o" + "-" * (x - 2) + "o"
    middle = "|" + " " * (x - 2) + "|"

    for row in range(y):
        if row == 0 or row == y - 1:
            print(top_bottom)
        else:
            print(middle)
