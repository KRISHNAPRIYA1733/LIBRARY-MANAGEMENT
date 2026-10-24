s=input("enter a string:")
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    print(i,count)