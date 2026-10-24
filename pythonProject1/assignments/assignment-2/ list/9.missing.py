n=int(input("enter the number of elements:"))
l=[]
for i in range(1,n):
    l.append(int(input()))
for i in range(1,n+1):
    if i not in l:
        print("missing number:",i)