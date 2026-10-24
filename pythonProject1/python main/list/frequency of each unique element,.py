l = [2, 4, 2, 6, 4, 2, 8, 6, 4]
visit=[]
new=[]
for i in l:
    if i not in visit:
        visit.append(i)
        new.append(l.count(i))
print(new)

