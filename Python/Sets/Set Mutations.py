n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
for _ in range(n2):
    a = list(input().split())
    s2 = set(map(int, input().split()))
    if(a[0]=="intersection_update"):
        s1.intersection_update(s2)
    elif(a[0]=="symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(a[0]=="difference_update"):
        s1.difference_update(s2)
    elif(a[0]=="update"):
        s1.update(s2)
print(sum(s1))
