def second(x):
    a = set(x) #Converting list into set
    a.remove(max(a)) # removed max element
    return max(a) #printing max element which is(max-1) of original

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split())) #Taking List values

print(second(x))
