def fib(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return a
n=int(input("enter a limi:"))
print(fib(n))