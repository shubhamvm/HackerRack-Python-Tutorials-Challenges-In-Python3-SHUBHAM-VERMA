n = int(input())
s = set(map(int, input().split()))
n1 = int(input())
for i in range(n1):
    cmd = list(input().split(' '))
    if (len(cmd) == 1):
        s.pop()
    else:
        value = int(cmd[1])
        s.discard(value)
print(sum(s))
