def print_formatted(n):
    s = len(bin(n)[2:])
    for i in range(1, n + 1):
        print(' '.join(map(lambda x: x.rjust(s), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
