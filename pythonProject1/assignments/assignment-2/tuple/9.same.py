t1=(1,4,7,10)
t2=(10,1,4,7)
count=0
for i in t1:
    if i in t2:
        count+=1
if count==len(t1) and len(t1)==len(t2):
    print("contains the elements")
else:
    print("dont have same elements:")