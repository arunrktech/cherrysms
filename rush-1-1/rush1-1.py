import sys

def rush(x, y):
    print(f"When calling rush({x}, {y}):")
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if x == 1:
            if row == 0 or row == y - 1:
                print("o")
            else:
                print("|")
        else:
            if row == 0 or row == y - 1:
                print("o" + "-" * (x - 2) + "o")
            else:
                print("|" + " " * (x - 2) + "|")
