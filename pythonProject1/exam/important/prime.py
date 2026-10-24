n=int(input("enter a limit:"))
m=int(input("enter ending:"))
for num in range(n,m+1):
    if num>1:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num)