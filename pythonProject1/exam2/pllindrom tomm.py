s=input("enter a string:")
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
if rev==s:
    print("pallindrome")
else:
    print("not a pallindromew")