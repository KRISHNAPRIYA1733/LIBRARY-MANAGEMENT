t=(2,4,8,6,10,1,4,7)
new=[]
for i in t:
    if t.count(i)>1:
        if i not in new:
            new.append(i)
print(new)