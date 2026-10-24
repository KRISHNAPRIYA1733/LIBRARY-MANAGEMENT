num=int(input("enter a three digit number:"))
temp=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if sum==temp:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
