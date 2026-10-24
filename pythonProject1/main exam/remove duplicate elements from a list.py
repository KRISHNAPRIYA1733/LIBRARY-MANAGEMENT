l=[4, 2, 4, 7, 2, 9, 7]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)