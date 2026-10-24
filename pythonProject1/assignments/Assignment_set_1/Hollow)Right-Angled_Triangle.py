#.......Hollow Right-Angled Triangle in Python
n=int(input("enter a limit:"))
for i in range(1,n+1):
    for j in range(i):
        if i==n or j==0 or j+1==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
