def find_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


def main():
    numbers = [2, 5, 1, -3, 15, -1, 6]
    print(f'список состоит из чисел: {numbers}')
    print(f'минимальное число из списка: {find_min(numbers)}')


if __name__ == '__main__':
    main()
