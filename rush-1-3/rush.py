import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    top    = "A" + "B" * (x - 2) + "A"
    bottom = "C" + "B" * (x - 2) + "C"
    middle = "B" + " " * (x - 2) + "B"
    full   = "B" * x

    for row in range(y):
        if x == 1 or y == 1:
            print(full)
        elif row == 0:
            print(top)
        elif row == y - 1:
            print(bottom)
        else:
            print(middle)
