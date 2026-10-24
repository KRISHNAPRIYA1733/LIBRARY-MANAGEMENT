s=input("enter a string:")
max=0
for i in range(len(s)):
    sub=""
    for j in range(i,len(s)):
        if s[j] not in sub:
            sub=sub+s[j]
        else:
            break
    if len(sub)>max:
        max=len(sub)
print("length:",max)