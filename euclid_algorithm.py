def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    print(gcd_subtraction(48, 18))


if __name__ == '__main__':
    main()
