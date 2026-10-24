s1={1,2,5,3,5,6}
s2={1,2,5,3}
count=0
for i in s1:
    if i in s2:
        count+=1
    else:
        count=0
if count==0:
    print("two set contains same elememts!")
else:
    print("it does not contain same elements")