from itertools import permutations
a,b = list(map(str,input().split()))
a = sorted(a)
for _ in list(permutations(a,int(b))):
    print(''.join(_))
