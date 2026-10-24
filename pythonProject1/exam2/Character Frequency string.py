s=input("enter a input:")
freq=""
for i in s:
    if i not in freq:
        print(i,"-",s.count(i))
        freq+=i
