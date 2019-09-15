n = int(input())
for _ in range(n):
    s = input()
    a,b = list(),list()
    for i in range(len(s)):
        a.append(s[i]) if i%2==0 else b.append(s[i])
    print("".join(a),"".join(b))
