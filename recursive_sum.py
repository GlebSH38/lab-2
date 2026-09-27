def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


def main():
    print(sum_to(5))


if __name__ == '__main__':
    main()
