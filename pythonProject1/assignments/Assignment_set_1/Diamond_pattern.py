#....5_Diamond pattern in Python
n=int(input("enter a limit:"))
for i in range(n):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for row in range(n-1,0,-1):
    for space in range(n-1-row+2):
        print(" ",end=" ")
    for column in range(2*row-1):
        print("*",end=" ")
    print()


