l=[4, 2, 7, 4, 2, 9, 4, 7]
visit=[]
for i in l:
    if i not in visit:
        print(i,":",l.count(i))
        visit.append(i)

