n=int(input("enter a limit:"))
a=0
b=1
for i in range(n+1):
    print(a)
    c=a+b
    a=b
    b=c
