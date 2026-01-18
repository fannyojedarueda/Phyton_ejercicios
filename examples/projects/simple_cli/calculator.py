"""Pequeña calculadora CLI"""

import argparse


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError('División por cero')
    return a / b


def main():
    parser = argparse.ArgumentParser(description='Calculadora simple')
    parser.add_argument('op', choices=['add', 'sub', 'mul', 'div'], help='operación')
    parser.add_argument('a', type=float, help='operando a')
    parser.add_argument('b', type=float, help='operando b')
    args = parser.parse_args()

    ops = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    result = ops[args.op](args.a, args.b)
    print(result)


if __name__ == '__main__':
    main()
