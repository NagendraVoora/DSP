file=open("f.txt","r")
small=open("small.txt","w")
upper=open("upper.txt","w")
nums=open("nums.txt","w")
symbols=open("symbols.txt","w")
k=file.read()
print(k)
for i in k:
    print(i)
    print(ord(i))
    if ord(i)>=65 and ord(i)<=90:
        upper.write(i)
    elif ord(i)>=97 and ord(i)<=122:
        small.write(i)
    elif ord(i)>=48 and ord(i)<=57:
        nums.write(i)
    else:
        symbols.write(i)
small.close()
upper.close()
nums.close()
symbols.close()
file.close()
