l=[0, 5, 0, 3, 8, 0, 2]
new=[]
zero=[]
for i in l:
    if i!=0:
        new.append(i)
    else:
        zero.append(i)
final=new+zero
print(final)

