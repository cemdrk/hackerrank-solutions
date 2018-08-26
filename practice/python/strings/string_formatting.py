def print_formatted(number):
    max_width = len(bin(number)[2:])
    for num in range(1, number + 1):
        print(' '.join(map(lambda x: x.rjust(max_width), [str(num), oct(num)[2:], hex(num)[2:].upper(), bin(num)[2:]])))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
