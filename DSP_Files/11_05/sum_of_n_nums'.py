#11/05/2022 
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

def display():
    print("hello")
display()

def fact(n):
    print("hello")
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
def fact(n):
    print("hi")
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
print(fact(n))

