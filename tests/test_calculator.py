import pytest
from src.calculator import calculate


def tests_plus():
    assert calculate('2+2') == 4


def test_plus_multiplication():
    assert calculate('2+2*2') == 6


def test_mod():
    assert calculate('3%2') == 1


def test_multiplication_unary():
    assert calculate('8*(-3)') == -24


def test_div():
    assert calculate('9//2') == 4


def test_multi_div():
    assert calculate('7*9/2') == 31.5


def test_power():
    assert calculate('8^2') == 64


def test_mod2():
    assert calculate('2%3') == 2


def tests_hard1():
    assert calculate('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3') == 3.001953125


def test_hard2():
    assert calculate('3^3*(-(3+8*2))/10') == -51.3


def test_exception_float():
    with pytest.raises(ValueError) as e:
        calculate('2+2.21.2')
    assert 'Неверный ввод числа с плавающей точкой: 2.21.2' == e.value.args[0]


def test_exception_floatmod():
    with pytest.raises(TypeError) as e:
        calculate('2%1.3')
    assert 'Невозможно вычислить результат операции % для данных типов 2 и 1.3' == e.value.args[
        0]


def test_exception_floatdiv():
    with pytest.raises(TypeError) as e:
        calculate('3.3//1.3')
    assert 'Невозможно вычислить результат операции // для данных типов 3.3 и 1.3' == e.value.args[0]


def test_exception_brackets():
    with pytest.raises(ValueError) as e:
        calculate('2+(3-4))')
    assert 'Недопустимый ввод выражения для вычисления' == e.value.args[0]


def test_exception_empty_input():
    with pytest.raises(ValueError) as e:
        calculate('')
    assert 'Ошибка: введена пустая строка' == e.value.args[0]


def test_exception_unavaliable_symbol():
    with pytest.raises(ValueError) as e:
        calculate('2#4')
    assert 'Неизвестный символ #' == e.value.args[0]


def test_exception_zero_division():
    with pytest.raises(ZeroDivisionError) as e:
        calculate('3/0')
    assert 'Деление / на нуль: 3 и 0' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
