# 1. Right-Angled Triangle Pattern in Python
n=int(input("enter a limit:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()