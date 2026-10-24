n=int(input("enter a num:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if sum==temp:
    print("arm")
else:
    print("ot arm")