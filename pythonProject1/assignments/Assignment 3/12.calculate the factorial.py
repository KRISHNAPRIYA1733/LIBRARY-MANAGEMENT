def facto(n):
    if n<0:
        print("enter a positive number!")
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)
n=int(input("enter a number:"))
facto(n)