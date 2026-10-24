d={"A":{1:20,2:30,3:40},"B":{4:10,5:50}}
key=0
value=0
for i in d:
    for j in d[i]:
        key+=1
        value+=1
print("no.of keys:",key)
print("no.of values:",value)