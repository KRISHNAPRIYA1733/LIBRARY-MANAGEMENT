s=[6,1,2,5,3,5,6]
s1=set()
for i in s:
    if i not in s1:
        s1.add(i)
l=list(s1)
print(s1)


