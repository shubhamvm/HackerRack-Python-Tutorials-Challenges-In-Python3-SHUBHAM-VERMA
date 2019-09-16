import string
def print_rangoli(size):
    mid = n - 1

    for i in range(n - 1, 0, -1):
        row = ['-'] * (2 * n - 1)
        for j in range(n - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))

    for i in range(0, n):
        row = ['-'] * (2 * n - 1)
        for j in range(0, n - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
