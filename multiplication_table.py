def main():
    for x in range(1, 11):
        line = ''
        for y in range(1, 11):
            line += str(x*y) + '\t'
        print(line)


if __name__ == '__main__':
    main()
