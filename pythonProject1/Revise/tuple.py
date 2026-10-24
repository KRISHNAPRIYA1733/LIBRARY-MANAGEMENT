#duplication remove
tup=(1,3,5,7,3,7)
new=[]
for i in tup:
    if i not in new:
        new.append(i)
print(new)
