
def division(num1: float | int, num2: float | int) -> float | int:
    if num2 == 0:
        raise ZeroDivisionError
    return num1/num2


def mod(num1: float | int, num2: float | int) -> int | float:
    if num2 == 0:
        raise ZeroDivisionError
    if int(num1) != num1 or int(num2) != num2:
        raise TypeError
    return num1 % num2


def int_div(num1: float | int, num2: float | int) -> int | float:
    if num2 == 0:
        raise ZeroDivisionError
    if int(num1) != num1 or int(num2) != num2:
        raise TypeError
    return num1 // num2


def power(num1: float | int, num2: float | int) -> float | int:
    if num1 == num2 == 0:
        raise ValueError
    return num1**num2
