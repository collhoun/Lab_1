from src.calculator import calculate


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    calculated_expression = ''
    while calculated_expression != 'quit':
        calculated_expression = input(
            "Введите выражение, результат которого вы хотите узнать (для завершения введите quit): ")
        try:
            result = calculate(calculated_expression)
            print(result)
        except ValueError as e:
            print(e)
        except ZeroDivisionError as zero:
            print(zero)
        except TypeError as t:
            print(t)


if __name__ == "__main__":
    main()
