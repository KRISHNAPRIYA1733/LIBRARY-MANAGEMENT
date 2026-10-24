s={33,52,31}
l=list(s)
large=l[0]
small=l[0]
for i in l:
    if i>large:
        large=i
    if i<small:
        small=i
print("largest:",large)
print("smallest:",small)