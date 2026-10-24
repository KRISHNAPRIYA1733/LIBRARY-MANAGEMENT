n=int(input("enter a number:"))
temp=n
result=0
while n>0:
    digit=n%10
    result=result*10+digit
    n=n//10
if temp==result:
    print("palindrome")
else:
    print("not a pallindrome")