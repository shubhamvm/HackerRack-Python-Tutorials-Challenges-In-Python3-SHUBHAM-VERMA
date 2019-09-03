a = int(input())
a1 = map(int,input().split())
a2 = set()
a2.update(a1)


c = int(input())
c1= map(int,input().split())
c2 = set()
c2.update(c1) #Entering value in set from user

b=a2^c2
for i in (sorted(b)): #printing in sorted format
    print(i)
