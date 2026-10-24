s1={1,2,5,3,5,6}
s2={1,2,5,3}
count=0
for i in s1:
    if i in s2:
        count+=1
if count==len(s2):
    print("subset!")
else:
    print("not subset!")