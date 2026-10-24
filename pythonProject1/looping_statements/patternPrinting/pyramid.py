row=int(input("enter the limit:"))
for i in range(row):
    for s in range(row-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()