from argparse import ArgumentError
import sys

def add(x, y):
    return x+y

def sub(x, y):
    pass

def mult(x, y):
    pass

def div(x, y):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ArgumentError("Incorrect Number of Arguments")
    
    x = sys.argv[1]
    y = sys.argv[2]

    if sys.argv[0].lower() == "add":
        print(add(x, y))

    if sys.argv[0].lower() == "sub":
        print(sub(x, y))

    if sys.argv[0].lower() == "mult":
        print(mult(x, y))

    if sys.argv[0].lower() == "div":
        print(div(x, y))