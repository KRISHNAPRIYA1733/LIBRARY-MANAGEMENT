s1={1,2,5,3,5,6}
s2={1,2,5,3}
s3={2,5,8}
s4=set()
for i in s1:
    if i in s2 and i in s3:
        s4.add(i)
print(s4)