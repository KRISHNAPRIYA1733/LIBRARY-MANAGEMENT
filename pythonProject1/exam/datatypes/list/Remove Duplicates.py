l=[34,24,5,89,2,98,65,42,34,5]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)