from src.operations import division, mod, power, int_div
ACCEPTABLE_OPERATORS: list = [
    '+', '-', '*', '//', '/', '^', '%', '(', ')', '@']


PRIORITY_OF_OPERANDS: dict = {'+': 1, '-': 1, '*': 2,
                              '/': 2, '//': 2, '%': 2, '^': 3, '(': 4, ')': 4}

OPERATIONS_WITH_NUMBERS: dict = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': division,
    '//': int_div,
    '%': mod,
    '^': power,
}
