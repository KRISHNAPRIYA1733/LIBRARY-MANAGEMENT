s1={1,2,5,3,5,6}
s2={3,5,9,0,33}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i)
print(s3)