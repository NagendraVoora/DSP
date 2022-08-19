int gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a==b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

n1=int(input("enter your first number:"))
n2=int(input("enter your second number:"))
if(gcd(n1,n2)==1):
    print("two are coprimes")
else:
    print("they are not coprimes")
