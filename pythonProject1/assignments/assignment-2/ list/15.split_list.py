l=[4,3,12,6,5,9,40,11]
a=[]
b=[]
mid=len(l)//2
for i in range(mid):
    a.append(l[i])
for i in range(mid,len(l)):
    b.append(l[i])
print("first half:",a)
print("second half:",b)
