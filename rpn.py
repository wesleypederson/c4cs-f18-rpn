#!/usr/bin/env python3
import operator

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv}

def calculate(arg):
    stack = arg.split()
    while len(stack) > 1:
        token = stack.pop()
        try:
            val = int(token)
            stack.append(val)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())
            func = op[token]
            result = func(val1, val2)
            stack.append(str(result))
    return int(stack[0])

def main():
    while True:
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()
