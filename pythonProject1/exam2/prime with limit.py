n=int(input("enter num1:"))
m=int(input("enter num2:"))
for num in range(n,m+1):
    if num>1:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
        if prime:
            print(num)