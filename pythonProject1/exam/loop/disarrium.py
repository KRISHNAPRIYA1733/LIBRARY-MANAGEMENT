n=int(input("enter a number:"))
sum=0
temp=n
length=len(str(n))
while n>0:
    digit=n%10
    sum=sum+digit**length
    n=n//10
    length-=1
if sum==temp:
    print("disarrium!")
else:
    print("not")