l=[3,5,2,3,42,90,68,5]
rep=[]
for i in l:
    if l.count(i)>1:
        if i not in rep:
            rep.append(i)
print(rep)