n=int(input("enter a number:"))
temp=n
sum=0
length=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**length
    n=n//10
    length-=1
if sum==temp:
    print(temp,"is adisarium number")
else:
    print(temp,"not a disarium number")
