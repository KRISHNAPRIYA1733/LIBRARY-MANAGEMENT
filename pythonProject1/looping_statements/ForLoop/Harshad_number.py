n=int(input("enter a number:"))
sum=0
for i in str(n):
    sum=sum+int(i)
print("sum of digits:",sum)
if n%sum==0:
    print("It is a Harshad Number...")
else:
    print("It is not a Harshad Number...")