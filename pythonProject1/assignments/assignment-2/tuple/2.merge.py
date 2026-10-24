tup1=("aa","abc","bc")
tup2=(1,5,7,3)
tup3=[]
for i in tup1:
        tup3.append(i)
for i in tup2:
        tup3.append(i)
tup3=tuple(tup3)
print(tup3)

