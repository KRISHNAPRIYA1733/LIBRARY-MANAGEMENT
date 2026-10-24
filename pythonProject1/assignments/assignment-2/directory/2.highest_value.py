d={1:20,2:30,3:40,4:90,5:5}
high=0
key=0
for i in d:
    if d[i]>high:
        high=d[i]
        key=i
print(key,":",high)