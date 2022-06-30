row=1
while row<=5:
    col=1
    while col<=5:
        if row==1 or col==1 or col==1+row*2 or row==5 or col==5-row*1+4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1            
          
