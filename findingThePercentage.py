from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    a=dict()    
    student_marks = {}
    if(n>1):
        for _ in range(n):
            c=0
            name, *line = input().split()
            scores = list(map(float, line))            
            student_marks[name] = scores
            for i in scores:
                c +=i                       
            av = c/3            
            a[name]=av            
    query_name = input()
print("{:.2f}".format(a[query_name])) 

