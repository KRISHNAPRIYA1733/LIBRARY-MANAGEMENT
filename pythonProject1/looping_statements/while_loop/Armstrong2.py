n=int(input("enter lower limit:"))
m=int(input("enter upper limit:"))
for i in range(n,m+1):
    temp=i
    sum=0
    length=len(str(i))
    while i>0:
        digit=i%10
        sum=sum+digit**length
        i=i//10
    if sum==temp:
        print(sum)






