def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        a = string[i:i+k]
        l = list(a)
        for i in l:
            for j in l[(l.index(i))+1:]:
                if(i == j):
                    p = a.rindex(j) 
                    del(l[p])
        b = "".join(l)
        print(b)

def gitsol(s,k):
    for i in range(len(s) // k):
        t = ''
        for c in s[i * k : (i + 1) * k]:
            if c in t:
                continue
            t += c
        print (t)
	
if __name__ == '__main__':
    string, k = input(), int(input())
    gitsol(string, k)
