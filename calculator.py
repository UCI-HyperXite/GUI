from argparse import ArgumentError
import sys

def add(x, y):
    pass

def sub(x, y):
    pass

def mult(x, y):
    pass

def div(x: int, y: int) -> float:
    """Divides the two numbers. Raises ValueError if the divisor is zero."""
    if y == 0:
        raise ValueError("Divisor cannot be zero")
    return x / y

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ArgumentError("Incorrect Number of Arguments")
    
    x = sys.argv[1]
    y = sys.argv[2]

    if sys.argv[0].lower() == "add":
        print(add(x, y))

    elif sys.argv[0].lower() == "sub":
        print(sub(x, y))

    elif sys.argv[0].lower() == "mult":
        print(mult(x, y))

    elif sys.argv[0].lower() == "div":
        print(div(x, y))
    
    else: raise ArgumentError("Invalid Operation")