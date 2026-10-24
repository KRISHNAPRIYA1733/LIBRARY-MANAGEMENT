n=[2,4,6,8]
m=[1,3,5,7,9]
o=[]
i=0
j=0
while i<len(n) and j<len(m):
    if n[i]<m[j]:
        o.append(n[i])
        i+=1
    else:
        o.append(m[j])
        j+=1
while i<len(n):
    o.append(n[i])
    i+=1
while j<len(m):
    o.append(m[j])
    j+=1
print(o)