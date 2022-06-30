row=5
n=1
while row>=n:
    col=5
    while col<=row-1:
        print(" ",end=" ")
        col=col-1
    j=1
    while  j<=row:
        print(row,end=" ")
        j=j+1
    print( )
    row=row-1