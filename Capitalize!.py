def solve(string):
    #result = a.title()  This is easiest method but it is not valid in this type of cases(3g , -2h , #n)
    #result = ' '.join(word[0].upper() + word[1:] for word in s.split())
    a = string.split(' ')
    b = ' '.join((word.capitalize() for word in a))
    return(b)
a = input()
result = solve(a)
print(result)
