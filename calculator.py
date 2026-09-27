def calculate(first, second, operator):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
    }
    operation = operations.get(operator)
    if operation is None:
        return None
    return operation(first, second)


def main():
    first_number = float(input('введите число: '))
    second_number = float(input('введите второе число: '))

    while True:
        operator = input('выберите действие (введите +, -, *, /): ')
        result = calculate(first_number, second_number, operator)

        if result is None:
            print('неверный ввод или деление на ноль')
        else:
            print(f'{first_number} {operator} {second_number} = {result}')
            break


if __name__ == '__main__':
    main()
