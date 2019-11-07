from itertools import combinations
a = int(input())
b = list(map(str,input().split()))
l = list(combinations(b,int(input())))
c = 0
for _ in l:
    if 'a' in _:
        c += 1
print((c)/len(l))
