row=1
while row<=5:
    col=1
    while col<=row:
        print(" ",end=" ")
        col=col+1
    b=2
    while b<=5-row:
        print("*",end=" ")
        b=b+1
    k=5
    while k>row:
        print("*",end=" ")
        k=k-1
    print( )
    row=row+1
