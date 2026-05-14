import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    top    = "/" + "*" * (x - 2) + "\\"
    bottom = "\\" + "*" * (x - 2) + "/"
    middle = "*" + " " * (x - 2) + "*"
    full   = "*" * x

    for row in range(y):
        if y == 1:
            print(full)
        elif row == 0:
            print(top)
        elif row == y - 1:
            print(bottom)
        else:
            print(middle)
