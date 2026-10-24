l=[2,4,6,3,43,68,3,33,57]
even=0
odd=0
for i in range(len(l)):
    if l[i]%2==0:
        even+=1
    else:
        odd+=1
print("even=",even)
print("odd",odd)