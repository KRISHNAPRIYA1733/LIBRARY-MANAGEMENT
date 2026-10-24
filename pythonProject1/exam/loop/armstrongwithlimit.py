n=int(input("enter starting:"))
m=int(input("enter ending:"))
for num in range(n,m+1):
    temp=num
    sum=0
    length=len(str(num))
    while num>0:
        digit=num%10
        sum=sum+digit**length
        num=num//10
    if sum==temp:
        print(sum)