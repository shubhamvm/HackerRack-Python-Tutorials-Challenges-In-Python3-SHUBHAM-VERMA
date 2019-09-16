a = set(map(int,input().split()))
n = int(input())
c = set()
for _ in range(n):
    b = set(map(int,input().split()))
    for i in b:
        c.add(i)
print(a.issuperset(c))
