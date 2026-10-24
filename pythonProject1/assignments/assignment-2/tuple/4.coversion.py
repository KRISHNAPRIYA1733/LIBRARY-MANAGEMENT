tup=(1,5,7,3)
t=list(tup)
new=[]
for i in tup:
    if i not in new:
        new.append(i)
print(new)