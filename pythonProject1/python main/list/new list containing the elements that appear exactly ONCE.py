l = [10, 25, 10, 30, 25, 40, 10, 50]
visit=[]
once=[]
for i in l:
    if l.count(i)==1:
        once.append(i)
    else:
        visit.append(i)
print(once)

