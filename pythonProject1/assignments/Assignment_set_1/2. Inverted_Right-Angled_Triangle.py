#.....2_Inverted Right-Angled Triangle in Python
n=int(input("enter a limit:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()