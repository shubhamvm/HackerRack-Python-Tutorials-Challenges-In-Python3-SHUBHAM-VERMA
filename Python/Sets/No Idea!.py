temp = input().split
a = list(map(int,input().split()))
b = set(map(int,input().split()))
c = set(map(int, input().split()))
h=0
for i in a:
    if(i in b):
        h+=1
    if(i in c):
        h-=1
print(h)
