n, m = map(int,input().split())
d1, d2 = list(), list()
for i in range(n):
    a = input()
    d1.append(a)
for i in range(m):
    b = input()
    d2.append(b)
for i in d2:
    c = 0
    for j in d1:
        if i == j:
            c += 1 
    if(c != 0):
        z = -1
        for k in range(c):
            if (z+1 != len(d1)):
                z = d1.index(i, z+1, len(d1))
                print(z+1, end = " ")
        print()
    else :
        print("-1")
