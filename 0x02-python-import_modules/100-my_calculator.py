#!/usr/bin/python3
"""My Calculator"""
if __name__ == "__main__":
    import argparse
    from calculator_1 import add, sub, mul, div
  
    parser = argparse.ArgumentParser()
    parser.add_argument("a", help="First Number", type=int)
    parser.add_argument("operator", help="operations", type=str)
    parser.add_argument("b", help="second number", type=int)

    args = parser.parse_args()
    a = int(args.a)
    b = int(args.b)
    operator = args.operator
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
