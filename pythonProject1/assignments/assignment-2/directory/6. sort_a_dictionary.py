d={1:20,2:30,3:40,7:92,9:23,5:43}
k=list(d.keys())
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i]>k[j]:
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
for i in k:
    print(i,":",d[i])