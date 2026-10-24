def addition(n,m):
    return n+m
def difference(n,m):
    return n-m
def multiplication(n,m):
    return n*m
def divison(n,m):
    return n/m
print("A.addition")
print("B.subtrsction")
print("C.multiplication")
print("D.division")
n=int(input("enter first number:"))
m=int(input("enter second number:"))
choice=input("enter you choice:")
if choice=='A' or choice=='a':
    print(addition(n,m))
elif choice=='B' or choice=='b':
    print(difference(n,m))
elif choice=='C' or 'c':
    print(multiplication(n,m))
elif choice=='D' or choice=='d':
    print(divison(n,m))
else:
    print("invalid choice...")
