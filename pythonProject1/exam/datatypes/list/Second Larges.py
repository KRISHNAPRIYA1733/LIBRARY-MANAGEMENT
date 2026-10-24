l=[34,24,5,89,2,98,65,42]
large=l[0]
small=l[0]
for i in l:
    if i>large:
        small=large
        large=i
    elif i>small and i!=large:
        small=i
print(small)

