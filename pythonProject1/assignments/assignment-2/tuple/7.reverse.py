t=(2,4,8,6,10,1,4,7)
new=[]
for i in range(len(t)-1,-1,-1):
    new.append(t[i])
new=tuple[new]
print(new)