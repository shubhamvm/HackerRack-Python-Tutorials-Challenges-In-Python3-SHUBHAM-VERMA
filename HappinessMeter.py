n,m = int,input().split


a = int,input().split()
print(len(a)+1)
if(n ==len(a)+1):
    a1 = set()
    a1.update(a)
else:
    a1={0}

b= int,input().split()
if(m ==len(b)+1):
    b1 = set()
    b1.update(b) #Entering value in set from user
else:
    b1={0}

c = int, input().split()
if(m==len(c)+1):
    c1 =set()
    c1.update(c)
else:
    c1={0}

h=0
for i in a1:
    for j in b1:
        if(i==j):
            h+=1
    for k in c1:
        if(i==k):
            h-=1
print(h)
