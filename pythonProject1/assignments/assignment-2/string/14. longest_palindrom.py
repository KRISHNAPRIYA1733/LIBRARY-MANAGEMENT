s=input("enter a string:")
longer=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if sub==sub[::-1]:
            if len(sub)>len(longer):
                longer=sub
print("longest pallindrome substring:",longer)