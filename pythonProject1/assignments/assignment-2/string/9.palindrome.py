s=input("enter a string:")
r=""
for i in s:
    r=i+r
if s==r:
    print("pallindrome")
else:
    print("not a pallindrome")