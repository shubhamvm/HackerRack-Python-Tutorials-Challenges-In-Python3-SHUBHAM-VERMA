n = int(input())
for _ in range(n):
    n1 = int(input())
    a = set(map(int,input().split()))
    n2 = int(input())
    b = set(map(int,input().split()))
    print(a.issubset(b))
