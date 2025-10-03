from src.constants import OPERATIONS_WITH_NUMBERS


def check_expression_correction(expr: str) -> bool:
    """

    Args:
        expr (str): string expression

    Returns:
        bool: True if there are no bad tokens in expr else False
    """
    for bad_token in do_bad_tokens():
        if bad_token in expr:
            return False

    if expr.count('(') != expr.count(')'):
        return False
    return True


def check_operation_correction(num1: float | int, num2: float | int, operation: str) -> tuple:
    """

    Args:
        num1 (float | int): first number
        num2 (float | int): second number
        operation (str): operation between number1 and number2

    Returns:
        tuple: returns a tuple of (bool, Exseption) to share information
    """
    if operation in ['/', '%', '//'] and num2 == 0:
        return False, ZeroDivisionError

    elif operation in ['%', '//'] and (num1 != int(num1) or num2 != int(num2)):
        return False, TypeError

    if operation == '^' and num1 == num2 == 0:
        return False, ValueError

    return True, Exception


def do_bad_tokens() -> list:
    """

    Returns:
        list: list of bad tokens
    """
    bad_tokens = []
    for i in OPERATIONS_WITH_NUMBERS:
        bad_tokens.append(f'({i})')
        bad_tokens.append(f'{i})')
    for i in OPERATIONS_WITH_NUMBERS:
        for j in OPERATIONS_WITH_NUMBERS:
            if i == j == '/':
                continue
            bad_tokens.append(i+j)
    return bad_tokens


if __name__ == '__main__':
    for i, v in enumerate(do_bad_tokens()):
        if v == '//':
            print(i, v)
