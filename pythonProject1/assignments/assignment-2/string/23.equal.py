s1="hello"
s2="hello"
flag=1
if len(s1) !=len(s2):
    flag=0
else:
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            flag=0
            break
if flag==1:
    print("strings are same")
else:
    print("strings are not same")