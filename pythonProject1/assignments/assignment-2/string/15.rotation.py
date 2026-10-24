a=input("enter a string:")
b=input("enter second string:")
if len(a)==len(b) and b in a+a:
    print("rotation")
else:
    print("not rotation")