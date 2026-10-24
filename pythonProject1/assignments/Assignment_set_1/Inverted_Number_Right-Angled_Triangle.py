#.... Inverted Number Right-Angled Triangle pattern in Python
n=int(input("enter a limit:"))
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()