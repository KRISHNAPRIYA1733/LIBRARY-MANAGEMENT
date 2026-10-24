s1={1,2,5,3,5,6}
s2={33,52,31}
count=0
for i in s1:
    if i in s2:
        count+=1
    else:
        count=0
if count==0:
    print("disjoint")
else:
    print("not disjoint")