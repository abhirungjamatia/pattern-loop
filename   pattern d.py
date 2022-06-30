a=1
while a<=5:
    b=1
    while b<=5:
        if a==b or a==5 or b==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print( )
    a=a+1