s="ammu anu priya dev adhi ammu priya"
word=s.split()
l=[]
for i in word:
    if i not in l:
        l.append(i)
for i in l:
    print(i,end=" ")