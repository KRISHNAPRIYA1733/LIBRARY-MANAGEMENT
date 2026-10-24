n=int(input("enter a num:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum*10+digit
    n=n//10
if temp==sum:
    print("pallindome")
else:
    print("not")