a=[1,2,3,4,5,6]
b=[6,5,1,8,9]
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(a[i])
print(c)