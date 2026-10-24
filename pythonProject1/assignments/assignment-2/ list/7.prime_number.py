l=[3,4,2,4,5,7,21,17,33,40]
for i in l:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)