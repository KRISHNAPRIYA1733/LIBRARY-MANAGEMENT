s1="bat"
s2="hat"
flag=1
if len(s1)!=len(s2):
    flag=0
else:
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            if s1[i]==s1[j] and s2[i]!=s2[j]:
                flag=0
            if s1[i]!=s1[j] and s2[i]==s2[j]:
                flag=0
if flag==1:
    print("isomophic")
else:
    print("not isomoephic")