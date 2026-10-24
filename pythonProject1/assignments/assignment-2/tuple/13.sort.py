t=(2,4,8,6,10,1,5,7)
l=list(t)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
l=tuple(l)
print(l)