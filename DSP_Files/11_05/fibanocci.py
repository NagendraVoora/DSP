def fibanocci(n):
    n1=0
    n2=1
    for i in range(0,n+1):
        if i==0:
            print("0",end=" ")
        elif i==1:
            print("1",end=" ")
        else:
            print(str(n1+n2),end=" ")
            n1,n2=n2,n1+n2
fibanocci(8)

print(" "  )
def fibanocci_before_n(n):
    n1=0
    n2=1
    print("0 ",end=" ")
    while(n2<=n):
        print(str(n2),end=" ")
        n1,n2=n2,n1+n2
fibanocci_before_n(10)


        
