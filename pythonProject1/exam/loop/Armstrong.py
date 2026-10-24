n=int(input("enter a limit:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("not armstrong")