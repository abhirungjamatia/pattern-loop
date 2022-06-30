row=1
while row<=5:
    col=1
    while col<=4:
        if row==1 or row==5 or col==1 or col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print( )
    row=row+1