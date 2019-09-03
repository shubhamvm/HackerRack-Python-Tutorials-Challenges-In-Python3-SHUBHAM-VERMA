def fun():
    a = int(input("Enter Lower Range: "))
    b = int(input("Enter Upper Range: "))
    if(a>0 and b>0):
        for i in range(a,b+1):
            n = 0
            for j in range(1,i):
                if((i%j)==0):
                    n=n+j
            if(n==i):
              print(i)
    else:
        print("Enter positive numbers please")
        fun()

fun()
