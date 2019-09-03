
    for i in range(1,Rows+1):
        for j in range(1,Columns+1):
            if (i ==1 or j==1 or i==Rows or j==Columns):
                print("*",end="")
            else:
                print(" ",end="")
        print()

    for i in range(1,Rows+1):
        for j in range(1,Columns+1):
            print("*",end="")
        print()



Rows = int(input("Enter Rows: "))
Columns = int(input("Enter Columns: "))
