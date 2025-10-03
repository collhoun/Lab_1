ACCEPTABLE_OPERATORS: list = [
    '+', '-', '*', '//', '/', '^', '%', '(', ')', '@']


PRIORITY_OF_OPERANDS: dict = {'+': 1, '-': 1, '*': 2,
                              '/': 2, '//': 2, '%': 2, '^': 3, '(': 4, ')': 4}

OPERATIONS_WITH_NUMBERS: dict = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '//': lambda x, y: x//y,
    '%': lambda x, y: x % y,
    '^': lambda x, y: x**y,
}

EXSEPTIONS_DESCRIPTIONS: dict = {ZeroDivisionError: lambda num1,
                                 num2, operation: f'Деление {operation} на нуль: {int(num2) if int(num2) == num2 else num2} и {int(num1) if int(num1) == num1 else num1}',
                                 TypeError: lambda num1, num2, operation: f'Невозможно вычислить результат операции {operation} для данных типов {int(num2) if int(num2) == num2 else num2} и {int(num1) if int(num1) == num1 else num1}',
                                 ValueError: lambda num1, num2, operation: f'Некорректная операция {operation} для операндов {int(num2) if int(num2) == num2 else num2} и {int(num1) if int(num1) == num1 else num1}'}
