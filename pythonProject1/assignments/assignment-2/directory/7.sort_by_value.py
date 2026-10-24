d={1:20,2:30,3:40,7:92,9:23,5:43}
k=list(d)
n=[]
for i in k:
    n.append(d[i])
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
for i in range(len(k)):
    print(k[i],":",n[i])