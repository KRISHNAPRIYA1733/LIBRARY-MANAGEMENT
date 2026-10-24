n=input("enter a string:")
m=input("enter second string:")
if len(n)!=len(m):
    print("not an anagram")
else:
    count=0
    for i in n:
        if n.count(i)==m.count(i):
            count+=1
    if count==len(n):
            print("anagram")
    else:
        print("not anagram")
