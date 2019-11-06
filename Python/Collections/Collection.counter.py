n= int(input())
ss = list(map(int,input().split()))
l = list()
for _ in range(int(input())):
    l.append(list(map(int,input().split())))
a = 0
for _ in l:
    if _[0] in ss:
        a += _[1]
        ss.remove(_[0])                
print(a)
