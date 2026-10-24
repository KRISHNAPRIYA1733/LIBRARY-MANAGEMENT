n=int(input("enter a number"))
if n<0:
    print("please enter a positive number!")
elif n==0:
    print("number is zero")
else:
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==1:
        print("not prime number")
    else:
        print("prime")
