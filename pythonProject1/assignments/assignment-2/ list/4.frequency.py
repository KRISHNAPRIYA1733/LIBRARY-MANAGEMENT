l=["aa","ab","abc","bb","ab"]
new=[]
for i in l:
    if i not in new:
        print(i,l.count(i))
        new.append(i)
