from itertools import combinations_with_replacement
a,b = list(map(str,input().split()))
a = sorted(a)
for _ in list(combinations_with_replacement(a,int(b))):
    print(''.join(_))
