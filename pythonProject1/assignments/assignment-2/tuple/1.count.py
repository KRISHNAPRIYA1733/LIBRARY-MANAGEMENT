tup=("aa","bb",5,"cd",12,5)
d={}
for i in tup:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)