from itertools import combinations
a,b = list(map(str,input().split()))
a = sorted(a)
for j in range(1,int(b)+1):
    for _ in list(combinations(a,j)):
        print(''.join(_))
