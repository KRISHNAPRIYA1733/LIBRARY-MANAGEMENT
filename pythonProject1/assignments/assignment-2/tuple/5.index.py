t=(2,4,8,6,10,1,4,7)
n=int(input("enter the element:"))
for i in range(len(t)):
    if t[i]==n:
        print("index:",i)
        break
else:
    print("not found!")