n=int(input("enter a number:"))
sum=0
temp=n
for i in str(n):
    sum=sum+int(i)
if n%sum==0:
    print("harshad")
else:
    print("not")