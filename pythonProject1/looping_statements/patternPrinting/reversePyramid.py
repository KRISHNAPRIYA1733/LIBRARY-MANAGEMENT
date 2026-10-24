n=int(input("enter the limit:"))
for i in range(n,0,-1): #when n=3
    for s in range(n-i):    # n-i=5-5=0
        print(" ",end=" ")  #so space=0
    for j in range(2*i-1):  #2*5-1=9
        print("*",end=" ")  #9 stars will print
    print()                 #next line
