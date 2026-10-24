n=int(input("enter a limit:"))
temp=n
sum=0
length=len(str(n))
while n>0:
    digit=n%10
    sum=sum+digit**length
    n=n//10
    length-=1
if sum==temp:
    print("disarrium")
else:
    print("not")