import itertools
k, m = map(int,input().split())
a = []
for i in range(k):
    ar = list(map(int,input().split()))
    a.append(ar[1:])

b = itertools.product(*a)
result = 0
for i in b:   
    result = max(sum([x*x for x in i])%m,result)
print(result)
