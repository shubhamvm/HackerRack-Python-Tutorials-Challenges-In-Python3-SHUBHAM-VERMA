d = dict()
n = int(input())
for _ in range(n):
    a,b = input().split()
    d[a]=b
for _ in range(n):
    i = str(input())
    print(i+"="+d[i]) if (i in d) else print("Not found")
