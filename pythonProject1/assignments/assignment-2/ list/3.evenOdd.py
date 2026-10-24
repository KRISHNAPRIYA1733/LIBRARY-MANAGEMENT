n=input("enter elements:").split()
even=[]
odd=[]
for i in n:
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print("even",even)
print("odd",odd)