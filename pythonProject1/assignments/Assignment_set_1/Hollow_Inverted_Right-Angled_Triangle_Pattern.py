#......Hollow Inverted Right-Angled Triangle Pattern

n=int(input("enter the limit:"))
for i in range(n,0,-1):
    for j in range(i):
        if j==0 or i==n or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()