row=1
while row<=5:
    col=1
    while col<=5:
        if row==1 or row==5 or row==3 or col==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print( )
    row=row+1