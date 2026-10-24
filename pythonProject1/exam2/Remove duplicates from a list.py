l= [1, 2, 2, 3, 4, 4, 5]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)