
from src.constants import ACCEPTABLE_OPERATORS, PRIORITY_OF_OPERANDS, OPERATIONS_WITH_NUMBERS, EXSEPTIONS_DESCRIPTIONS
from src.correction import check_expression_correction, check_operation_correction


def tokenization(expr: str) -> list:
    """
    Args:
        expr (str): main expression with operands and operators

    Raises:
        ValueError: ValueError if there is wrong operand in expr or two-more '.' in token

    Returns:
        list: list of all tokens
    """
    if not expr or not (expr.strip()):
        raise ValueError('Ошибка: введена пустая строка')
    if not check_expression_correction(expr):
        raise ValueError('Недопустимый ввод выражения для вычисления')
    if '@' in expr:
        raise ValueError('Неизвестный символ @')

    tokens = []
    ind = 0
    expr = expr.replace(' ', '')
    expr = expr.replace('//', '@')
    current_token = ''

    while ind < len(expr):
        if expr[ind].isdigit() or expr[ind] == '.':
            current_token += expr[ind]
            ind += 1
            continue

        elif expr[ind] in ACCEPTABLE_OPERATORS:
            if current_token:
                if current_token.count('.') > 1:
                    raise ValueError(
                        f'Неверный ввод числа с плавающей точкой: {current_token}')
                tokens.append(current_token)
                current_token = ''
            tokens.append(expr[ind])
            ind += 1

        else:
            raise ValueError(f'Неизвестный символ {expr[ind]}')
    if current_token and current_token.count('.') <= 1:
        tokens.append(current_token)
    elif current_token and current_token.count('.') > 1:
        raise ValueError(
            f'Неверный ввод числа с плавающей точкой: {current_token}')

    for i, value in enumerate(tokens):
        if value == '@':
            tokens[i] = '//'
    return tokens


def make_rpn(tokens: list) -> list:
    """

    Args:
        tokens (list): list of tokens that consists of numbers and operators

    Returns:
        list: create rpn from tokens list
    """
    out_list = []
    stack = []
    tokens = insert_zeroes(tokens)

    for char in tokens:
        if char.replace('.', '').isdigit():
            out_list.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack[-1] != '(':
                out_list.append(stack.pop(-1))
            stack.pop(-1)

        elif char in ACCEPTABLE_OPERATORS:
            if stack and '(' not in stack and PRIORITY_OF_OPERANDS[char] > PRIORITY_OF_OPERANDS[stack[-1]]:
                stack.append(char)
            elif stack and '(' not in stack and PRIORITY_OF_OPERANDS[char] <= PRIORITY_OF_OPERANDS[stack[-1]]:
                out_list.append(stack.pop(-1))
                stack.append(char)
            elif stack and '(' in stack:
                stack.append(char)
            elif stack:
                out_list.append(stack.pop(-1))
                stack.append(char)
            else:
                stack.append(char)

    while stack:
        out_list.append(stack.pop(-1))

    return out_list


def count_rpn(expr: list) -> float:
    """

    Args:
        expr (list): list expression of tokens (numbers and operators) in rpn

    Returns:
        flaot: returns a float result of calculating expression written in rpn
    """
    stack = []
    answer = 0.0
    for char in expr:
        if char.replace('.', '').isdigit():
            stack.append(char)
        elif len(stack) > 1:
            num1 = float(stack.pop(-1))
            num2 = float(stack.pop(-1))
            check_operation = check_operation_correction(num2, num1, char)
            if check_operation[0]:
                answer = do_operation(num1, num2, char)
                stack.append(answer)
            else:
                raise check_operation[1](
                    EXSEPTIONS_DESCRIPTIONS[check_operation[1]](num1, num2, char))

    return int(answer) if int(answer) == answer else answer


def do_operation(number1: float | int, number2: float | int, operator: str) -> float | int:
    """

    Args:
        number1 (float): first number
        number2 (float): second number
        operator (str): operator (action with two nums)

    Returns:
        float: returns float result of operation between town numbers
    """
    return OPERATIONS_WITH_NUMBERS[operator](number2, number1)


def insert_zeroes(tokens: list) -> list:
    """
    This function if needed to define the unary operators

    Args:
        tokens (list): list of tokens created from func "tokenization"

    Returns:
        list: list of tokens with inserted zeroes
    """
    if tokens[0] == '-' or tokens[0] == '+':
        tokens.insert(0, '0')

    for i, value in enumerate(tokens):
        if tokens[i] == '(' and len(tokens) > i+1 and tokens[i+1] == '-':
            tokens.insert(i+1, '0')
        elif tokens[i] == '(' and len(tokens) > i+1 and tokens[i+1] == '+':
            tokens.insert(i+1, '0')

    return tokens


def calculate(expr):
    """

    Args:
        expr (_type_): string expression user want to calculate

    Returns:
        _type_: calculated result of expression
    """
    return count_rpn(make_rpn(tokenization(expr)))


if __name__ == '__main__':
    expr = '*'
    print(tokenization(expr))
    print(make_rpn(tokenization(expr)))
    print(count_rpn(make_rpn(tokenization(expr))))
