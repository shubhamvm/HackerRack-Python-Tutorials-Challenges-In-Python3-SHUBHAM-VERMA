if __name__ == '__main__':
    l = list()
    p=set()
    for _ in range(int(input())):
        _ = dict()
        
        name = input()
        score = float(input())
       # _.append(name)
      #  _.append(score)
       # p.append(score)
        #if(score>=0)and not(name ==" "):
        _[score]=name
        p.add(score)
        l.append(_)
        
p.remove(min(p))
a= min(p)
b = list()
for i in l:
    for j in i:
        if(j==a):
            b.append(i[a])
b.sort()
for z in b:
    print(z)
