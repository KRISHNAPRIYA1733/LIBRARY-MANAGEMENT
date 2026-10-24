n=int(input("enter a number:"))
sum=0
for i in str(n):
    sum=sum+int(i)
if n%sum==0:
    print("harshad number!")
else:
    print("not")