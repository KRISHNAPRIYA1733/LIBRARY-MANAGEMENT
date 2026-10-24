l=[2,1,2,1,2,2,3,3]
visit=[]
for i in l:
    if i not in visit:
        print(i,"->",l.count(i))
    visit.append(i)

