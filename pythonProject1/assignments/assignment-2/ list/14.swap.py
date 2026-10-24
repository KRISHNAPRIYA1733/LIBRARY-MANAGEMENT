l=[4,6,10,44,30,50]
temp=l[0]
l[0]=l[len(l)-1]
l[len(l)-1]=temp
print(l)