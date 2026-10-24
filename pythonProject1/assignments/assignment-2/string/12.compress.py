s=input("enter a string:")
i=0
while i<len(s):
    count=1
    while i< len(s)-1 and s[i]==s[i+1]:
        count+=1
        i+=1
    print(s[i],count,sep="",end=" ")
    i+=1
