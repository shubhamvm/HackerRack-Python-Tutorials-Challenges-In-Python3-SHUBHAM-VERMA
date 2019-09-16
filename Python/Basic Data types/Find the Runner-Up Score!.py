def second(x):
    a = set(x)
    a.remove(max(a))
    return max(a)

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))

print(second(x))
