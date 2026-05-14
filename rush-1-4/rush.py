import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    print(f"When calling rush({x}, {y}):")

    for row in range(y):
        if x == 1 or y == 1:
            print("B" * x)
        else:
            if row == 0 or row == y - 1:
                print("A" + "B" * (x - 2) + "C")
            else:
                print("B" + " " * (x - 2) + "B")
