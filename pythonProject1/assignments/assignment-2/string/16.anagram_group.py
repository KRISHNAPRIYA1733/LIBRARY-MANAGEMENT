s=["listen","tab","silent","bat"]
new=[]
for i in s:
    if i  not in new:
        print(i,end=" ")
        for j in s:
            if len(i)==len(j):
                count=0
                for ch in i:
                    if i.count(ch)==j.count(ch):
                        count+=1
                if count==len(i):
                    print(j,end=" ")
                    new.append(j)
        print()